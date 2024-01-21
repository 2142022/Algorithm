import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# DFS로 각 부분 수열 구하기
# idx: 수열의 인덱스
# cnt: 경계선 개수
def dfs(idx, cnt):
    global N, S, case

    # 4개의 부분 수열로 나눈 경우
    if cnt == 3:
        # 모두 유효한 경계선인 경우
        if idx < N:
            return 1
        return 0

    # 수열을 모두 탐색했지만 부분 수열이 4개가 아닌 경우
    if idx == N:
        return 0

    # 이미 탐색한 경우, 기존 경우의 수 반환
    if dp[idx][cnt] != -1:
        return dp[idx][cnt]
    dp[idx][cnt] = 0

    # 경계선을 세울 수 있는 경우
    if prefix[idx] == (cnt + 1) * S:
        dp[idx][cnt] += dfs(idx + 1, cnt + 1)
    # 경계선을 긋지 않고 다음 탐색
    dp[idx][cnt] += dfs(idx + 1, cnt)

    return dp[idx][cnt]

##############################################################################################

# 수열의 길이
N = int(input())

# 수열
A = list(map(int, input().split()))

# 누적합
prefix = [0] * N
prefix[0] = A[0]
for i in range(1, N):
    prefix[i] = prefix[i - 1] + A[i]

# 각 부분 수열의 합
# 4의 배수가 아니라면 끝내기
S = prefix[-1]
if S % 4:
    print(0)
    exit()
S //= 4

# dp[i][c]: i번째 원소에서 c개의 경계선을 그었을 때(c + 1개의 부분 수열 존재) 가능한 경우의 수
dp = [[-1] * 4 for _ in range(N)]

# DFS로 각 부분 수열 구하기
print(dfs(0, 0))