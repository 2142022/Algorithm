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

print('%.3f' % max(dp))

# 다음과 같이 쓰면 틀림
# 반례: 1.0이 들어오면 1.0으로 출력됨 (정답: 1.000)
# print(round(max(dp), 3))
