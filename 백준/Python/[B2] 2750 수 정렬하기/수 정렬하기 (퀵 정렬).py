import sys
input = sys.stdin.readline

# 현재 범위 내에서 pivot(맨 앞 원소)의 위치 찾기
def get_pivot(pivot_idx, end):
    # pivot
    pivot = nums[pivot_idx]

    # 탐색 시작점
    start = pivot_idx + 1
    while start <= end:
        # 앞에서부터 pivot보다 큰 값 찾기
        while start <= end and nums[start] <= pivot:
            start += 1

        # 뒤에서부터 pivot보다 작은 값 찾기
        while start <= end and nums[end] > pivot:
            end -= 1

        # 두 값의 위치 바꾸기
        if pivot_idx < start <= end:
            nums[start], nums[end] = nums[end], nums[start]

    # pivot값 위치 바꾸기
    nums[pivot_idx], nums[start - 1] = nums[start - 1], nums[pivot_idx]

    return start - 1

#################################################################################

# 퀵 정렬
def quick_sort(start, end):
    if start >= end:
        return

    # 맨 앞 원소의 인덱스 구하기
    idx = get_pivot(start, end)

    # pivot의 좌우 분할하여 탐색
    quick_sort(start, idx - 1)
    quick_sort(idx + 1, end)

#################################################################################

# 수 개수
N = int(input())

# N개의 수
nums = [int(input()) for _ in range(N)]

# 퀵 정렬
quick_sort(0, N - 1)

print(*nums, sep = '\n')