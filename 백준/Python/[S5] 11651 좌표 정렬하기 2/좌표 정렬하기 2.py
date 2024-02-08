import sys
input = sys.stdin.readline

N = int(input())
pos = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))
for i in pos:
    print(*i)