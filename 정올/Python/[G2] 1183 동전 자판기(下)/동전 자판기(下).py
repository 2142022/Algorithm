import sys
input = sys.stdin.readline

# idx번째 동전 사용하기
# p: 현재까지의 사용한 동전으로 만든 가격
def use(idx, p):
    # 모든 동전을 다 탐색한 경우
    if idx == -1:
        # 원하는 가격을 만든 경우
        if p == W:
            return 1
        return 0

    # 현재 동전의 가격
    v = price[idx]

    # 현재 동전이 사용할 수 있는 개수
    for c in range(coins[v], -1, -1):
        # W 이하인 경우만 탐색
        if p + v * c <= W:
            cnt[idx] = c
            if use(idx - 1, p + v * c):
                return 1

    return 0

###################################################################################

# 가격
W = int(input())

# 각 동전의 개수
price = (500, 100, 50, 10, 5, 1)
coins = {i: j for i, j in zip(price, list(map(int, input().split())))}

# 사용한 동전의 개수
cnt = [0] * 6

# 동전 하나씩 사용하기
use(5, 0)

print(sum(cnt))
print(*cnt)