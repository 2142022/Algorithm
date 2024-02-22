import sys
input = sys.stdin.readline

# 구매하려고 하는 카드 개수
N = int(input())

# 각 카드팩 가격
P = [0] + list(map(int, input().split()))

# cost[i]: 카드 i개를 샀을 때의 최대 금액
cost = [0] * (N + 1)
for i in range(1, N + 1):
    # 카드팩
    for j in range(1, i + 1):
        cost[i] = max(cost[i], cost[i - j] + P[j])

print(cost[N])