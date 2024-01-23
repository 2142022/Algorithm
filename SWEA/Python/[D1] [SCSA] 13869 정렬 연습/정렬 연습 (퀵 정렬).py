# 탐색 구간의 첫 원소의 위치 찾기 (Hoare 분할 알고리즘)
def partition(start, end):
    pivot = nums[start]
    i, j = start + 1, end
    while True:
        # 앞에서부터 탐색: pivot보다 작은 값은 패스
        while i < end and nums[i] < pivot:
            i += 1

        # 뒤에서부터 탐색: pivot보다 큰 값은 패스
        while j > start and nums[j] > pivot:
            j -= 1

        # 앞, 뒤 모두 정렬된 경우 끝내기
        if j <= i:
            break

        # i, j swap
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    # pivot 위치 바꾸기
    nums[start], nums[j] = nums[j], nums[start]

    return j

#######################################################

# 퀵 정렬 - 수열의 start부터 end까지 정렬
def quick_sort(start, end):
    if start < end:
        # pivot을 기준으로 분할
        pivot = partition(start, end)
        quick_sort(start, pivot - 1)
        quick_sort(pivot + 1, end)

#######################################################

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 수열 크기
    N = int(input())

    # 수열
    nums = list(map(int, input().split()))

    # 퀵 정렬
    quick_sort(0, N - 1)

    print(f'#{t}', end = ' ')
    for num in nums:
        print(num, end = ' ')
    print()