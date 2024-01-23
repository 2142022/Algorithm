# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 일 수
    N = int(input())

    # N일 동안의 매매가
    sales = list(map(int, input().split()))

    # 최대 이익
    plus = 0

    # 상한가
    mx = sales[-1]
    for i in range(N - 2, -1, -1):
        # 오늘 매매가
        price = sales[i]

        # 상한가보다 작다면 이익
        if price < mx:
            plus += mx - price

        # 상한가보다 크다면 상한가 바꾸기
        elif price > mx:
            mx = price

    print(f'#{t} {plus}')