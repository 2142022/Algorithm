import sys
input = sys.stdin.readline

# (i, j)를 지나는 시작 세로선과 도착 세로선이 같은지 확인
# (i, j + 1)도 확인
def is_finish(i, j):
    for t in range(2):
        # 시작 세로선 찾기
        r, c = i, j + t
        while r > 0:
            # 올라가기
            r -= 1

            # 왼쪽에 사다리가 있는 경우, 왼쪽으로 이동
            if board[r][c] == 2:
                c -= 1
            # 오른쪽에 사다리가 있는 경우, 오른쪽으로 이동
            elif board[r][c] == 1:
                c += 1
        start = c

        # 도착 세로선 찾기
        r, c = i, j + 1 - t
        while r <= H:
            # 내려가기
            r += 1

            # 왼쪽에 사다리가 있는 경우, 왼쪽으로 이동
            if board[r][c] == 2:
                c -= 1
            # 오른쪽에 사다리가 있는 경우, 오른쪽으로 이동
            elif board[r][c] == 1:
                c += 1
        end = c

        # 시작과 다른 세로선인 경우 끝내기
        if start != end:
            finish[start] = 0
        else:
            finish[start] = 1

########################################################################

# cnt번째 사다리 추가하기
# start: 마지막으로 추가한 가로선 다음부터 시작
def draw(cnt, start):
    global min_cnt, finish

    # 아직 연결되지 않은 세로선의 개수
    not_finish = N - sum(finish)

    # 완성된 경우 끝내기
    if not_finish == 0:
        min_cnt = min(cnt, min_cnt)
        if min_cnt <= 1:
            return 1
        return 0

    # 남은 깊이(depth)로 가로선을 추가해도 완성되지 않는 경우 끝내기
    if not_finish >= (min_cnt - cnt) * 2:
        return 0

    # 가로선을 추가해도 최소 수 이상인 경우 끝내기
    if cnt + 1 >= min_cnt:
        return 0

    # 현재 추가할 가로선
    for i in range(start, len(pos)):
        # 가로선 시작 위치
        r, c = pos[i]

        # 이전 사다리와 연속되지 않는지 확인
        if board[r][c] or board[r][c + 1]:
            continue

        # 추가
        board[r][c], board[r][c + 1] = 1, 2
        origin = finish[:]
        is_finish(r, c)

        # 다음 가로선 추가
        if draw(cnt + 1, i + 1):
            return 1

        # 현재 가로선 취소
        board[r][c] = board[r][c + 1] = 0
        finish = origin[:]

    return 0

########################################################################

# 사다리 세로선 수, 가로선 수, 높이
N, M, H = map(int, input().split())

# 사다리 가로선 체크 (왼쪽: 1, 오른쪽: 2)
board = [[0] * (N + 1) for _ in range(H + 2)]
# 원래 본인 위치로 돌아오는 세로선 체크
finish = [1] * (N + 1)
finish[0] = 0
for _ in range(M):
    # 가로선 위치, 세로선 시작 위치
    a, b = map(int, input().split())
    board[a][b], board[a][b + 1] = 1, 2
    is_finish(a, b)

# 추가할 수 있는 사다리 위치 구하기
pos = []
for i in range(1, H + 1):
    for j in range(1, N):
        if not board[i][j] and not board[i][j + 1]:
            pos.append((i, j))

# 추가하는 최소 가로선 수
min_cnt = 4
draw(0, 0)

# 불가능한 경우 -1 출력
if min_cnt == 4:
    print(-1)
else:
    print(min_cnt)