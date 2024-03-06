import sys
input = sys.stdin.readline

# (r, c)의 대각선에 물이 있는 바구니의 개수 구하기
def get_cnt(r, c):
    cnt = 0
    for d in (1, 3, 5, 7):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc]:
            cnt += 1
    return cnt

##########################################################################

# 비바라기 시전
# start: 구름 현재 위치
def rain(start):
    # 구름 이동 위치
    clouds = set()

    # 모든 구름이 이동 및 물의 양 증가
    for r, c in start:
        nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
        clouds.add((nr, nc))
        board[nr][nc] += 1

    # 대각선에 물이 있는 바구니의 개수만큼 물의 양 증가
    for r, c in clouds:
        board[r][c] += get_cnt(r, c)

    # 다음 구름의 시작 위치
    nclouds = set()
    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and (r, c) not in clouds:
                board[r][c] -= 2
                nclouds.add((r, c))

    return nclouds

##########################################################################

# 격자 크기, 명령 횟수
N, M = map(int, input().split())

# 각 바구니에 있는 물의 양
board = [list(map(int, input().split())) for _ in range(N)]

# 8방 탐색용
dr, dc = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)

# 처음 구름의 위치
clouds = {(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)}

# 명령
for i in range(M):
    # 방향, 거리
    d, s = map(int, input().split())
    d -= 1

    # 비바라기 시전
    clouds = rain(clouds)

# 모든 바구니에 들어있는 물의 양 합 구하기
res = 0
for b in board:
    res += sum(b)
print(res)