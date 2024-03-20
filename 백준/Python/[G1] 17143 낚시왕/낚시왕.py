import sys
input = sys.stdin.readline

# c열에 있는 상어 잡기
def fishing(c):
    # 땅에서 가장 가까운 상어 찾기
    size = 0
    for r in range(R):
        if board[r][c][0] != -1:
            size = board[r][c][2]
            board[r][c] = [-1, -1, -1]
            break
    return size

#####################################################################

# 이동 후 위치, 방향 구하기
# x: 현재 위치
# d: 현재 방향
# dist: 이동 거리
# L: (가로 / 세로 길이) - 1
def get_pos(x, d, dist, L):
    # 방향 전환 횟수, 이동 후 위치
    cnt, nx = divmod(x + dist, L)

    # 방향 전환
    if cnt % 2:
        d = (d + 2) % 4
        nx = L - nx

    return nx, d

#####################################################################

# 상어 이동
def move():
    global board

    # 상어별 이동하고 난 후의 보드
    after = [[[-1, -1, -1]] * C for _ in range(R)]

    # 보드 탐색
    for r in range(R):
        for c in range(C):
            # 속력, 방향, 크기
            s, d, z = board[r][c]

            # 상어가 없는 경우 패스
            if s == -1:
                continue

            # 이동 후 위치 (상하)
            if d % 2 == 0:
                nr, d = get_pos(r, d, dr[d] * s, R - 1)
                nc = c

            # 이동 후 위치 (좌우)
            else:
                nc, d = get_pos(c, d, dc[d] * s, C - 1)
                nr = r

            # 저장할 위치에 상어가 없는 경우 저장
            # 이미 상어가 있는 경우, 작은 상어가 있을 때만 저장
            if after[nr][nc][2] < z:
                after[nr][nc] = [s, d, z]

    # 보드 바꾸기
    board = after

#####################################################################

# 격자 크기, 상어 수
R, C, M = map(int, input().split())

# 각 칸에 있는 상어의 속도, 방향, 크기
board = [[[-1, -1, -1]] * C for _ in range(R)]
for _ in range(M):
    # 위치, 속력, 방향, 크기
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d = {1: 0, 2: 2, 3: 1, 4: 3}[d]
    board[r][c] = [s, d, z]

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 낚시 왕이 잡은 상어 크기의 합
score = 0

# C번 이동
for j in range(C):
    # 상어 잡기
    score += fishing(j)

    # 상어 이동
    move()

print(score)