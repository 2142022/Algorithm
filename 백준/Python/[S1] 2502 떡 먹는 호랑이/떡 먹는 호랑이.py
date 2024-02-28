import sys
input = sys.stdin.readline

# 할머니가 넘어온 날, 그 날 호랑이에게 준 떡의 개수
D, K = map(int, input().split())

# 피보나치 수열 F[i]: 1, 1, 2, 3, 5, 8, ...
F = [0] * D
F[1] = 1
for i in range(2, D):
    F[i] = F[i - 1] + F[i - 2]

# 첫째 날 준 떡의 개수: A, 둘째 날 준 떡의 개수: B
# D째 날 준 떡의 개수: A X F[D - 2] + B X F[D - 1]
# x: F[D - 2], y: F[D - 1]
x = F[D - 2]
y = F[D - 1]

# 첫째 날 준 떡의 개수
A = B = 0
for i in range(1, K):
    # 둘째 날 준 떡의 개수
    if (K - i * x) % y == 0:
        A = i
        B = (K - i * x) // y
        break

print(A, B, sep = '\n')