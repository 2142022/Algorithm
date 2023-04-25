import sys
input = sys.stdin.readline

# 유제품의 수
N = int(input())

# N개의 유제품의 가격
price = []
for _ in range(N):
    price.append(int(input()))

# 내림차순 정렬
price.sort(reverse = True)

# N개의 유제품을 모두 살 때 필요한 최소 비용
result = 0

# 3번째 유제품은 무료
for i in range(N):
    if i % 3 == 2:
        continue
    else:
        result += price[i]

print(result)