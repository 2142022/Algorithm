import sys
input = sys.stdin.readline

# 병사 수
N = int(input())

# 병사의 전투력
power = list(map(int, input().split()))

# 병사 전투력 순서
order = [1] * N

for i in range(N):
    for j in range(i+1, N):
        # 기준 병사의 전투력보다 작다면
        if power[i] > power[j]:
            # 기준 병사의 순서보다 작거나 같다면
            if order[j] < order[i] + 1:
                order[j] = order[i] + 1

print(N - max(order))
