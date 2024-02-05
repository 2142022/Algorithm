import sys
input = sys.stdin.readline

# 표의 크기, 합을 구해야 하는 횟수
N, M = map(int, input().split())

# 표
nums = [list(map(int, input().split())) for _ in range(N)]

# 누적합
prefix = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix[i][j] = nums[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

# 합 구하기
for _ in range(M):
    # (x1, y1)부터 (x2, y2)까지 합
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix[x2][y2] - prefix[x2][y1 - 1] - prefix[x1 - 1][y2] + prefix[x1 - 1][y1 - 1])

