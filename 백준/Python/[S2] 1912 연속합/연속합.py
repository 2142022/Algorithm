import sys
input = sys.stdin.readline

# 최대 연속합 구하기
def get_max():
    # 수열의 크기가 1이라면 그대로 반환
    if n == 1:
        return nums[0]

    # dp[i][0]: i번째 숫자를 포함하지 않았을 때, 최대 연속합
    # dp[i][1]: i번째 숫자를 포함했을 때, 최대 연속합
    dp = [[0] * 2 for _ in range(n)]
    dp[0] = [0, nums[0]]
    # nums[0]이 음수인 경우를 대비하여 dp[1]도 초기화
    dp[1] = [nums[0], max(nums[0], 0) + nums[1]]

    # dp[i][0]: 이전까지의 최대 연속합 저장
    # dp[i][1]: 전부터 이어지는 연속합과 현재 숫자부터 새로 연속합을 시작하는 경우 비교
    for i in range(2, n):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = max(dp[i - 1][1], 0) + nums[i]

    return max(dp[n - 1])

##################################################################################

# 수열 크기
n = int(input())

# 수열
nums = list(map(int, input().split()))

# 최대 연속합 구하기
print(get_max())
