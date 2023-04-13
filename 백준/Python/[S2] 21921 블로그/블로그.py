import sys
input = sys.stdin.readline

# N: 블로그 사용 일수, X: 확인할 기간
N, X = map(int, input().split())

# N일 동안의 방문자 수
visitant = list(map(int, input().split()))

# 최대 방문자 수
max_cnt = 0

# X일 전부터 현재까지의 누적 방문자 수
dp = [0] * N
# 현재까지의 누적합
now = 0
for i in range(N):
    # X일 이전에는 더하기
    if i < X - 1:
        now += visitant[i]
    elif i == X - 1:
        now += visitant[i]
        dp[i] = now
        max_cnt = max(max_cnt, dp[i])
    else:
        now += visitant[i] - visitant[i - X]
        dp[i] = now
        max_cnt = max(max_cnt, dp[i])

# 최대 방문자 수가 0이라면 SAD 출력
if max_cnt == 0:
    print('SAD')
else:
    print(max_cnt)
    print(dp.count(max_cnt))