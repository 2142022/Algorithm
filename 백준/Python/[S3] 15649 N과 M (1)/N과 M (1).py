import sys
input = sys.stdin.readline

# 숫자 고르기
def get_comb():
    # 모든 숫자를 고른 경우 끝내기
    if len(nums) == M:
        print(*nums)
        return

    # 숫자 고르기
    for i in range(1, N + 1):
        # 아직 뽑지 않은 수인 경우, 선택
        if i not in nums:
            nums.append(i)
            get_comb()
            nums.pop()

##################################################

# 최대 자연수, 수열 크기
N, M = map(int, input().split())

# 수열
nums = []

# 재귀로 숫자 하나씩 고르기
get_comb()