import sys
input = sys.stdin.readline

# 퇴사까지 남은 기간
N = int(input())

# 상담 기간과 상담 수익 입력받기
consult = []
for i in range(N):
    consult.append(list(map(int, input().split())))

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    # 상담 기간이 퇴사날을 넘어가는 경우에는 그 다음날 상담 수익 그대로
    if i + consult[i][0] > N:
        dp[i] = dp[i + 1]
    # 그렇지 않을 경우 최대 수익 비교
    else:
        dp[i] = max(dp[i + 1], dp[i + consult[i][0]] + consult[i][1])

print(dp[0])
