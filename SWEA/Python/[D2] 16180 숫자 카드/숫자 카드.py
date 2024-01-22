from collections import Counter

# 테스트케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 카드 수
    N = int(input())

    # N개의 수
    a = list(map(int, input()))

    # 각 수의 개수
    cnt = dict(Counter(a))

    # 가장 많은 카드의 숫자와 장 수
    n, c = sorted(cnt.items(), key = lambda x : (-x[1], -x[0]))[0]

    print(f'#{t} {n} {c}')