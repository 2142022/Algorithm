from collections import deque
import sys
input = sys.stdin.readline

# (r, c) 절벽이 가로와 세로로 교차하는지 확인
def cross(r, c):
    # 사방에 절벽이 있는지 확인
    up = down = left = right = 0
    if r - 1 >= 0 and board[r - 1][c] == 0:
        up = 1
    if r + 1 < N and board[r + 1][c] == 0:
        down = 1
    if c - 1 >= 0 and board[r][c - 1] == 0:
        left = 1
    if c + 1 < N and board[r][c + 1] == 0:
        right = 1

    if (up or down) and (left or right):
        return True
    return False

###########################################################################################################

# 견우와 직녀가 만나는 최소 시간
def get_time():
    # 각 위치까지 견우가 갈 수 있는 최소 시간 (0, 1: 새로운 오작교를 건넌 여부)
    time = [[[2000] * 2 for _ in range(N)] for _ in range(N)]
    time[0][0] = [0, 0]

    # 탐색 위치, 새로 지은 오작교 건넌 횟수, 바로 직전에 건넜는지 체크를 담은 큐
    q = deque([(0, 0, 0, 0)])
    while q:
        # 현재 위치, 방문 체크, 세로 지은 오작교 건넌 횟수, 바로 직전에 건넜는지 체크
        r, c, f, p = q.popleft()

        # 직녀가 있는 곳에 도달한 경우 끝내기
        if r == c == N - 1:
            continue

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 절벽 교차 지점 패스
            if board[nr][nc] == -1:
                continue

            # 땅 (항상 갈 수 있음)
            if board[nr][nc] == 1 and time[r][c][f] + 1 < time[nr][nc][f]:
                time[nr][nc][f] = time[r][c][f] + 1
                q.append((nr, nc, f, 0))

            # 절벽 (오작교 주기가 될 때까지 기다리기)
            elif board[nr][nc] == 0 and not f and not p:
                nt = time[r][c][f] + M - time[r][c][f] % M
                # 절벽이 가로와 세로로 교차하는 지점은 건널 수 없음
                if nt < time[nr][nc][1]:
                    time[nr][nc][1] = nt
                    q.append((nr, nc, 1, 1))

            # 오작교 (오작교 주기가 될 때까지 기다리기)
            elif board[nr][nc] >= 2 and not p:
                nt = time[r][c][f] + board[nr][nc] - time[r][c][f] % board[nr][nc]
                if nt < time[nr][nc][f]:
                    time[nr][nc][f] = nt
                    q.append((nr, nc, f, 1))

    return min(time[N - 1][N - 1])

###############################################################################################################

# 지형 크기, 새로 만들어지는 오작교 주기
N, M = map(int, input().split())

# 지형
board = [list(map(int, input().split())) for _ in range(N)]

# 가로와 세로로 교차하는 절벽 체크
for i in range(N):
    for j in range(N):
        if board[i][j] == 0 and cross(i, j):
            board[i][j] = -1

# 견우와 직녀가 만나는 최소 시간
print(get_time())

