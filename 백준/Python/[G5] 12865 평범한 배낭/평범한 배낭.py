import sys
input = sys.stdin.readline

# N: 물품의 수, K: 버틸 수 있는 무게
N, K = map(int, input().split())

# (N+1) X (K+1) 크기의 리스트
dp = [[0] * (K + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    # 물품의 무게와 가치 입력받기
    w, v = map(int, input().split())

    for j in range(1, K + 1):
        # 무게보다 작은 열은 이전 행값과 동일하게 채우기
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 무게 이상의 열
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])
