# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 수열의 길이
    N = int(input())

    # 0을 기준으로 분리해서 연속된 1 저장
    nums = list(input().split('0'))

    # 가장 긴 수열 개수
    cnt = 0
    for i in nums:
        cnt = max(cnt, len(i))

    print(f'#{t} {cnt}')