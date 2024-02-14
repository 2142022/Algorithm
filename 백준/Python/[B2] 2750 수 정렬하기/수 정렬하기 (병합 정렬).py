import sys
input = sys.stdin.readline

# 병합 정렬
def merge_sort(lst):
    # 원소가 1개인 경우 그대로 리턴
    if len(lst) == 1:
        return lst

    # 반으로 나누기
    idx = len(lst) // 2
    left = merge_sort(lst[:idx])
    right = merge_sort(lst[idx:])

    # 좌우 원소 하나씩 비교하면서 정렬
    result = []
    i, j = 0, 0
    while i < idx and j < len(lst) - idx:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소들 이어서 추가
    if i != idx:
        result += left[i:]
    else:
        result += right[j:]

    return result

###########################################################

# 수 개수
N = int(input())

# N개의 수
nums = [int(input()) for _ in range(N)]

# 병합 정렬
result = merge_sort(nums)

print(*result, sep = '\n')