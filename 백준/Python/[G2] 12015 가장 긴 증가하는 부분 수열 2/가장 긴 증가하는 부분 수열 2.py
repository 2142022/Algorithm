from bisect import bisect_left
import sys
input = sys.stdin.readline

# 수열 크기
N = int(input())

# 가장 긴 증가하는 부분 수열
nums = []

# 수열 탐색
for num in list(map(int, input().split())):
    # 현재 원소가 지금까지 탐색한 수 중 가장 큰 수인 경우 수열에 추가
    if not nums or num > nums[-1]:
        nums.append(num)

    # 현재 원소가 가장 긴 증가하는 수열의 중간에 들어가는 수인 경우
    else:
        # 들어갈 수 있는 위치 찾기
        # 위치: 같은 값의 가장 왼쪽
        nums[bisect_left(nums, num)] = num

print(len(nums))