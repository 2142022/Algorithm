import sys
input = sys.stdin.readline

# 양의 실수 개수
N = int(input())

# dp: 현재까지 곱의 결과와 현재값과 비교
dp = [0] * N
dp[0] = float(input())

for i in range(1, N):
    # 현재값
    num = float(input())
    dp[i] = max(dp[i - 1] * num, num)

print(f'{max(dp):.3f}')