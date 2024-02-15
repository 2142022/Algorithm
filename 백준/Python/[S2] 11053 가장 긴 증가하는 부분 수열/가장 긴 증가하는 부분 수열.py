import sys
input = sys.stdin.readline

# 수열 크기
N = int(input())

# 수열
A = list(map(int, input().split()))

# 증가하는 부분 체크
dp = [1] * N
for i in range(N - 1):
    num = A[i]

    # i번째 수 이후 숫자가 i번째 수보다 큰 경우 확인
    for j in range(i + 1, N):
        if A[j] > num:
            # 기존의 증가하는 수열과 현재 증가하는 수열 비교
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))