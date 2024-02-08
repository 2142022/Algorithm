import sys
input = sys.stdin.readline

N = int(input())
pos = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))
for i in pos:
    print(*i)