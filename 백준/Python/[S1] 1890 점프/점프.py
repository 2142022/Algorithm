import sys
input = sys.stdin.readline

# NXN 크기의 게임판
N = int(input())

# 게임판 정보
board = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: (i, j)까지 이동하는 경로의 수
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

# 수학에서 격자모양 판(그래프 1사분면)에서 경로의 수를 구하는 방법 생각하기
# 현재 점 = 왼쪽 점까지 가는 경우의 수 + 아래 점까지 가는 경우의 수
for i in range(N):
    for j in range(N):
        # 종착점(N-1, N-1)에 도착하면 멈추기
        if i == N - 1 and j == N - 1:
            break

        # 오른쪽으로 이동해도 범위를 벗어나지 않으면 이동
        if j + board[i][j] < N:
            dp[i][j + board[i][j]] += dp[i][j]
        # 아래로 이동해도 범위를 벗어나지 않으면 이동
        if i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]

print(dp[N - 1][N - 1])