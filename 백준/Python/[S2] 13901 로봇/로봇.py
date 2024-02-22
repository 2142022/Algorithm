import sys
input = sys.stdin.readline

# 로봇 이동
def go(r, c, d):
    while True:
        # 더 이상 갈 곳이 없는 경우 회전
        nr, nc = r + dr[dir[d]], c + dc[dir[d]]
        if not (0 <= nr < R and 0 <= nc < C) or board[nr][nc] != 0:
            for _ in range(4):
                d = (d + 1) % 4
                nr, nc = r + dr[dir[d]], c + dc[dir[d]]
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 0:
                    break

            # 사방이 막혀 있는 경우
            else:
                print(r, c)
                return

        # 현재 방향으로 이동
        r += dr[dir[d]]
        c += dc[dir[d]]
        board[r][c] = 1

################################################################################

# 방 크기
R, C = map(int, input().split())

# 방
board = [[0] * C for _ in range(R)]

# 장애물 체크
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = -1

# 로봇 위치
r, c = map(int, input().split())
board[r][c] = 1

# 이동 방향 순서
dir = list(map(lambda x: int(x) - 1, input().split()))

# 현재 이동 방향
d = 0

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 더 이상 이동할 수 있는 곳이 없을 때까지 이동
go(r, c, d)

