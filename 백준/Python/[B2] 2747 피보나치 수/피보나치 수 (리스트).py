import sys
input = sys.stdin.readline

# 구할 피보나치 수
n = int(input())

# 피보나치 수
F = [0] * (n + 1)
F[1] = 1
for i in range(2, n + 1):
    F[i] = F[i - 1] + F[i - 2]

print(F[n])