import sys
input = sys.stdin.readline

# 동전 수, 만들 가치 합
n, k = map(int, input().split())

# 만들 수 있는 가치의 경우의 수
dp = [0] * (k + 1)
dp[0] = 1
for _ in range(n):
    # 현재 동전의 가치
    v = int(input())

    # 만들 수 있는 가치
    for i in range(k + 1):
        if i - v >= 0:
            dp[i] += dp[i - v]

print(dp[k])