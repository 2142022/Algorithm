import sys
input = sys.stdin.readline

# N: 단원의 개수, T: 공부할 수 있는 시간
N, T = map(int, input().split())

dp = [[0] * (T + 1) for _ in range(N + 1)]

# 각 단원별 정보 입력받고 값 비교하기
for i in range(1, N + 1):
    # K: 예상 공부 시간, S: 문제의 배점
    K, S = map(int, input().split())

    for j in range(1, T + 1):
        # 예상 공부 시간보다 작으면 이전 값과 동일하게 채우기
        if j < K:
            dp[i][j] = dp[i - 1][j]

        # 문제의 배점 이상이면 최대값 비교하기
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - K] + S)

print(dp[N][T])