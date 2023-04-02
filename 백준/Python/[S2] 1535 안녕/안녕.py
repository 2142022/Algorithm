import sys
input = sys.stdin.readline

# 사람의 수
N = int(input())

# 인사할 때마다 잃는 체력
L = list(map(int, input().split()))

# 인사할 때마다 얻는 기쁨
J = list(map(int, input().split()))

# 세준이가 얻을 수 있는 최대 기쁨
dp = [[0] * 100 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(100):
        # 잃는 체력보다 작은 j는 이전 행값과 동일
        if j < L[i - 1]:
            dp[i][j] = dp[i - 1][j]
        # 체력을 쓸 수 있는 경우에는 체력을 쓰는 경우와 안 쓰는 경우 비교
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i - 1]] + J[i - 1])

print(dp[N][99])