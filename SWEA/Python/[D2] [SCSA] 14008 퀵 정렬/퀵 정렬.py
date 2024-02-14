# 현재 범위 내 맨 앞 원소의 위치 찾기
def get_pivot(pivot_idx, end):
    # 맨 앞 원소
    pivot = A[pivot_idx]

    # 탐색 시작점
    start = pivot_idx + 1
    while start <= end:
        # 앞에서부터 pivot보다 큰 값 찾기
        while start <= end and A[start] <= pivot:
            start += 1

        # 뒤에서부터 pivot보다 작은 값 찾기
        while start <= end and A[end] > pivot:
            end -= 1

        # 두 값의 위치 바꾸기
        if pivot_idx < start <= end:
            A[start], A[end] = A[end], A[start]

    # pivot 값의 위치 바꾸기
    A[pivot_idx], A[start - 1] = A[start - 1], A[pivot_idx]

    # pivot값의 위치 반환
    return start - 1

#################################################################

# 퀵 정렬
def quick_sort(start, end):
    # 모두 정렬된 경우 끝내기
    if start >= end:
        return

    # 현재 범위 내 맨 앞 원소의 위치
    idx = get_pivot(start, end)

    # pivot의 좌우로 분할하여 탐색
    quick_sort(start, idx - 1)
    quick_sort(idx + 1, end)

#################################################################

# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 정수 개수
    N = int(input())

    # N개의 정수
    A = list(map(int, input().split()))

    # 퀵 정렬
    quick_sort(0, N - 1)

    print(f'#{T} {A[N // 2]}')