import sys
input = sys.stdin.readline

# 상담 가능 기간
N = int(input())

# i번째 날까지 얻을 수 있는 수익
dp = [0] * (N + 1)
for i in range(1, N + 1):
    # 상담 기간, 금액
    T, P = map(int, input().split())

    # 현재까지의 최대 수익 저장
    dp[i] = max(dp[i], dp[i - 1])

    # 상담이 가능한 경우, 상담을 할 때의 수익과 하지 않을 때의 수익 비교
    if i + T - 1 <= N:
        dp[i + T - 1] = max(dp[i + T - 1], dp[i - 1] + P)

print(dp[N])