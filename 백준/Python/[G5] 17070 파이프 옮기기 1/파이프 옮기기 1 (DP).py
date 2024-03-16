import sys
input = sys.stdin.readline

# 집 크기
N = int(input())

# 집 상태
board = [list(map(int, input().split())) for _ in range(N)]

# 각 칸에 파이프(오른쪽 파이프의 위치)가 위치할 수 있는 방법의 수
# cnt[i][j][d]: (i, j)에 d 방향으로 파이프를 놓는 방법의 수 (0: 가로, 1: 세로, 2: 대각선)
cnt = [[[0] * 3 for _ in range(N)] for _ in range(N)]
for i in range(1, N):
    if board[0][i]:
        break
    cnt[0][i] = [1, 0, 0]

# 행
for i in range(1, N):
    # 열
    for j in range(1, N):
        # 현재 위치에 벽에 없는 경우
        if board[i][j] == 0:
            # 가로로 두기
            cnt[i][j][0] = cnt[i][j - 1][0] + cnt[i][j - 1][2]

            # 세로로 두기
            cnt[i][j][1] = cnt[i - 1][j][1] + cnt[i - 1][j][2]

            # 대각선으로 두기 (단, 위와 왼쪽도 빈 칸이어야 함)
            if board[i - 1][j] == 0 and board[i][j - 1] == 0:
                cnt[i][j][2] = sum(cnt[i - 1][j - 1])

print(sum(cnt[N - 1][N - 1]))