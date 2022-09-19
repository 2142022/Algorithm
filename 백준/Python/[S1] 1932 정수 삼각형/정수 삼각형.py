import sys
input = sys.stdin.readline

# 삼각형의 크기
n = int(input())

dp = [[0] * (n + 1) for i in range(n+1)]

for i in range(1, n + 1):
    # 한 줄씩 입력받기
    line = list(map(int, input().split()))

    for j in range(len(line)):
        # 왼쪽 대각선 위와 위를 비교하여 더 큰값을 더하기
        dp[i][j+1] = max(dp[i-1][j], dp[i-1][j+1]) + line[j]

print(max(dp[n]))
