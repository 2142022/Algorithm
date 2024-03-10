import sys
input = sys.stdin.readline

# 총 금액
X = int(input())

# 물건의 종류 수
N = int(input())

# 총 가격
price = 0

# 각 물건의 가격의 개수
for _ in range(N):
    a, b = map(int, input().split())
    price += a * b

if X == price:
    print('Yes')
else:
    print('No')