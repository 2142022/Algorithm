# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 배열 개수, 찾을 숫자
    N, D = map(int, input().split())

    # N개의 숫자
    nums = [0] + list(map(int, input().split()))

    # 찾을 숫자가 있는 범위
    start, end = 1, N
    while start <= end:
        # 범위 내 중간값
        mid = (start + end) // 2
        n = nums[mid]

        # 찾을 숫자인 경우 끝내기
        if n == D:
            print(f'#{T} {mid}')
            break

        # 찾을 숫자가 중간값보다 작은 경우
        if n > D:
            end = mid - 1

        # 찾을 숫자가 중간값보다 큰 경우
        else:
            start = mid + 1

    # 원하는 숫자를 못 찾은 경우
    else:
        print(f'#{T} 0')
