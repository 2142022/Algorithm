from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# (i, j)에서부터 연속적으로 블록 4개 추가하기
def get_block(i, j):
    # 가능한 모든 블록 모양
    pos = []

    # 방문 체크를 담은 큐
    q = deque([(1 << (10 * i + j), [(i, j)])])
    while q:
        vb, vl = q.popleft()

        # 사방 탐색
        for r, c in vl:
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                # 범위 체크
                if not (0 <= nr < 20 and 0 <= nc < 10):
                    continue

                # 이미 블록이 있는 경우 패스
                if board[nr][nc]:
                    continue

                # 방문 체크
                if vb & 1 << (10 * nr + nc):
                    continue
                nvb = vb | 1 << (10 * nr + nc)

                # 이미 확인한 모양인 경우 패스
                if nvb in check:
                    continue
                check.add(nvb)

                # 블록 4개를 모두 선택한 경우
                nvl = vl[:] + [(nr, nc)]
                if len(vl) == 3:
                    pos.append(nvl)
                    continue

                # 다음 위치 큐에 담기
                q.append((nvb, nvl))

    return pos

########################################################################################

# 현재 블록 모양으로 제거할 수 있는 줄 수 구하기
def remove(blocks):
    # 현재 블록의 각 행별 개수
    cnt = defaultdict(int)
    for i, j in blocks:
        cnt[i] += 1

    # 현재 블록 모양으로 제거할 수 있는 줄 수
    remove_cnt = 0

    # 각 행에서 블록이 10개가 된 경우 삭제
    for i, v in cnt.items():
        if sum(board[i]) + v == 10:
            remove_cnt += 1

    return remove_cnt

########################################################################################

# 0행까지 올라갈 수 있는지 확인
def possible(blocks):
    # 모든 블록의 위에 다른 블록이 없으면 가능
    for i, j in blocks:
        if i > starts[j]:
            return 0
    return 1

########################################################################################

# 제거할 수 있는 최대 줄 수 구하기
def get_cnt():
    # 제거할 수 있는 최대 줄 수
    max_cnt = 0

    # 블록 시작 지점
    for j in range(10):
        i = starts[j]

        # 연속적으로 블록 4개 추가하기
        pos = get_block(i, j)

        # 현재 블록 모양으로 제거할 수 있는 줄 수
        for blocks in pos:
            cnt = remove(blocks)

            # 기존보다 많이 삭제할 수 있는 경우, 0행까지 올라갈 수 있는지 확인
            if cnt > max_cnt and possible(blocks):
                max_cnt = cnt

                # 최대 개수인 4개를 삭제한 경우 끝내기
                if max_cnt == 4:
                    return max_cnt

    return max_cnt

########################################################################################

# 각 열별 시작 행
starts = [0] * 10

# 보드
board = []
for i in range(20):
    row = list(map(int, input().rstrip()))
    board.append(row)
    for j, info in enumerate(row):
        if info and not starts[j]:
            starts[j] = i - 1
for j in range(10):
    if not starts[j]:
        starts[j] = 19

# 탐색한 모양과 위치 체크
check = set()

# 제거할 수 있는 최대 줄 수
print(get_cnt())
