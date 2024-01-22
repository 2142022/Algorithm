# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 숫자 개수
    N = int(input())

    # 원래 숫자
    nums = list(map(int, input().split()))

    # 오름차순 정렬
    nums.sort()

    print(f'#{t}', end = ' ')
    for num in nums:
        print(num, end = ' ')
    print()
