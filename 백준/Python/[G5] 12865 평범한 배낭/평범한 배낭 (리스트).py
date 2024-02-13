import sys
input = sys.stdin.readline

# 물품 수, 버틸 수 있는 무게
N, K = map(int, input().split())

# dp[i][j]: i번째 물건까지 탐색했을 때, 총 무게가 j일 때의 최대 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    # 현재 물건의 무게, 가치
    W, V = map(int, input().split())

    # 무게가 j일 때의 최대 가치: 현재 물건을 포함하지 않는 경우와 현재 물건을 포함하는 경우 비교
    for j in range(K + 1):
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)

print(max(dp[-1]))