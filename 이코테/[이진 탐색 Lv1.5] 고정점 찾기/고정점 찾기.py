import sys
input = sys.stdin.readline

# 수열의 원소의 개수
N = int(input())

# 수열
nums = list(map(int, input().split()))

# 고정점
idx = -1

# 이진 탐색을 이용하여 고정점 찾기
start = 0
end = N - 1
while start <= end:
    mid = (start + end) // 2

    # 중간값과 인덱스가 같다면 고정점
    if nums[mid] == mid:
        idx = mid
        break
    # 중간값이 인덱스보다 작다면 이후 값들 탐색
    elif nums[mid] < mid:
        start = mid + 1
    # 중간값이 인덱스보다 크다면 이전 값들 탐색
    else:
        end = mid - 1

print(idx)