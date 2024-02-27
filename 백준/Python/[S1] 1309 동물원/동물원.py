import sys
input = sys.stdin.readline

# 우리 크기
N = int(input())

# 나눌 수
M = 9901

# i행에 사자를 두는 경우의 수
# (i-2행에 사자를 두는 경우의 수) * 3 + (i-1행에 사자를 두는 경우의 수) * 2
# 3: 사자를 두지 않는 경우, 왼쪽에 둔 경우, 오른쪽에 둔 경우
# 2: 사자를 두지 않는 경우, 반대쪽에 두는 경우
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 3
for i in range(2, N + 1):
    dp[i] = (3 * dp[i - 2] + 2 * (dp[i - 1] - dp[i - 2])) % M

print(dp[N])