# 병합 정렬
def merge_sort(nums):
    global cnt

    # 원소의 개수가 1개인 경우 그대로 리턴
    if len(nums) == 1:
        return nums

    # 좌우 나눠서 병합 정렬
    idx = len(nums) // 2
    left = merge_sort(nums[:idx])
    right = merge_sort(nums[idx:])

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 지 확인
    if left[-1] > right[-1]:
        cnt += 1

    # 정렬
    result = []
    i, j = 0, 0
    while i < idx and j < len(nums) - idx:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소 추가하기
    if i != idx:
        result += left[i:]
    else:
        result += right[j:]

    return result

#######################################################################

# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 정수 개수
    N = int(input())

    # N개의 정수
    a = list(map(int, input().split()))

    # 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    cnt = 0

    # 병합 정렬
    L = merge_sort(a)

    print(f'#{T} {L[N // 2]} {cnt}')