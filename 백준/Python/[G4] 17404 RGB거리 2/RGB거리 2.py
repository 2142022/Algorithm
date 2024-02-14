import sys
input = sys.stdin.readline

# 집 수
N = int(input())

# 각 집을 빨강, 초록, 파랑으로 칠하는 비용
cost = [list(map(int, input().split())) for _ in range(N)]

# 최종 최소 비용
min_cost = 1000 * N

# 1번 집의 색
for color in range(3):
    # dp[i][j]: i번째 집을 j번째 색으로 칠했을 때의 최소 비용
    # dp[0]은 1번 집을 현재 색으로 칠했을 때의 비용으로 초기화
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = [cost[0][color]] * 3

    # 2번 집부터 탐색
    for i in range(1, N):
        for j in range(3):
            # 2번 집과 마지막 집은 1번 집과 같은 색을 칠할 수 없음
            if (i == 1 or i == N - 1) and j == color:
                dp[i][j] = 1000 * N
                continue

            # 이전 집과 다른 색을 칠했을 때의 최솟값 저장
            dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + cost[i][j]

    # 최소 비용 비교
    min_cost = min(min_cost, min(dp[-1]))

print(min_cost)