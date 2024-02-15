import sys
input = sys.stdin.readline

# 구할 피보나치 수
n = int(input())

# i - 2번째 수, i - 1번째 수
a, b = 0, 1
for i in range(n - 1):
    num = a + b
    a, b = b, num

print(b)