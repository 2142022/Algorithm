from collections import defaultdict
import sys
input = sys.stdin.readline

# 성장: 4방에 나무가 있는 칸 수만큼 +
def grow():
    # 나무가 있는 칸
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                cnt = 0

                # 사방 탐색
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    # 범위 체크
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue

                    # 나무가 있는 경우
                    if board[nr][nc] > 0:
                        cnt += 1

                # 성장
                board[r][c] += cnt

###############################################################################################################

# 번식: 4방의 빈칸에 (현재 나무 수) // (빈칸 수) 만큼 +
def spread():
    # 최종 번식 위치
    pos = defaultdict(int)

    # 나무가 있는 칸
    for r in range(N):
        for c in range(N):
            # 현재 나무 수
            num = board[r][c]
            if num > 0:
                # 빈 칸 위치
                empty = []

                # 사방 탐색
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    # 범위 체크
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue

                    # 빈 칸인 경우
                    if board[nr][nc] == 0:
                        empty.append((nr, nc))

                # 빈 칸에 번식되는 나무 수
                plus = num // len(empty) if empty else 0
                for i, j in empty:
                    pos[(i, j)] += plus

    # 번식
    for k, v in pos.items():
        r, c = k
        board[r][c] += v

###############################################################################################################

# 제초제 뿌리기
def kill():
    # 가장 많이 박멸되는 나무 수와 그 때 제초제가 뿌려지는 위치
    max_cnt, max_pos = 0, []

    # 나무가 있는 칸
    for r in range(N):
        for c in range(N):
            # 박멸되는 나무 수
            cnt = board[r][c]
            if cnt > 0:
                # 제초제가 뿌려지는 위치
                pos = [(r, c)]

                # 4방 탐색
                for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    # K번 이동 가능
                    for k in range(1, K + 1):
                        nr, nc = r + dr * k, c + dc * k

                        # 범위 체크
                        if not (0 <= nr < N and 0 <= nc < N):
                            break

                        # 벽이 있는 경우 끝내기
                        if board[nr][nc] == -100:
                            break

                        # 제초제 뿌릴 위치 추가
                        pos.append((nr, nc))

                        # 제초제가 있거나 빈 칸인 경우 끝내기
                        if board[nr][nc] <= 0:
                            break

                        # 나무가 있는 경우, 박멸되는 나무 수 추가
                        cnt += board[nr][nc]

                # 제조체 위치 갱신
                if cnt > max_cnt:
                    max_cnt = cnt
                    max_pos = pos

    # 모든 제초제 남은 년 수 +1
    for i in range(N):
        for j in range(N):
            if -100 < board[i][j] < 0:
                board[i][j] += 1

    # 제초제 뿌리기
    for i, j in max_pos:
        board[i][j] = -C

    return max_cnt

###############################################################################################################

# 격자 크기, 박멸이 진행되는 년 수, 제초제 확산 범위, 제초제 지속 년 수
N, M, K, C = map(int, input().split())

# 각 칸의 나무 수, 벽 정보, 제초제 정보
# 1~: 나무 수
# 0: 빈 칸
# -1 ~ -C-1 : 제초제 남은 년 수
# -100: 벽
board = [list(map(lambda x: int(x) if int(x) != -1 else -100, input().split())) for _ in range(N)]

# 총 박멸한 나무 수
total = 0

# M년간 반복
for _ in range(M):
    # 성장: 4방에 나무가 있는 칸 수만큼 +
    grow()

    # 번식: 4방의 빈칸에 (현재 나무 수) // (빈칸 수) 만큼 +
    spread()

    # 제초제를 뿌렸을 때 박멸한 나무 수
    cnt = kill()

    # 박멸한 나무 수가 없다는 것은 더 이상 나무가 없다는 의미이므로 끝내기
    if cnt == 0:
        break
    total += cnt

print(total)