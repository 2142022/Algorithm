import sys
input = sys.stdin.readline

n = int(input())

# 0이나 1이면 q도 0이나 1
if n == 0 or n == 1:
    q = n
else:
    q = int(n ** 0.5)

    # 제곱했을 때 n이 아니면 +1
    if q * q < n:
        q += 1

print(q)

