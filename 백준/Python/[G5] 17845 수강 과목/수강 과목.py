import sys
input = sys.stdin.readline

# N: 최대 공부시간, K: 과목 수
N, K = map(int, input().split())

# dp[i][j]: i번째 과목을 수강했을 때, j시간동안 공부할 때 얻을 수 있는 최대 중요도
dp = [[0] * (N + 1) for _ in range(K + 1)]

# 한 과목씩 탐색
for i in range(1, K + 1):
    # I: 현재 과목의 중요도, T: 현재 과목에 필요한 공부시간
    I, T = map(int, input().split())

    # 시간별 중요도 구하기
    for j in range(1, N + 1):
        # T미만의 시간은 이전 과목과 동일
        if j < T:
            dp[i][j] = dp[i - 1][j]
        # T이상의 시간은 (T시간 이전의 중요도에서 현재 과목의 중요도 더한 값)과 이전 과목의 중요도 비교하기
        else:
            dp[i][j] = max(dp[i - 1][j - T] + I, dp[i - 1][j])

print(dp[K][N])
