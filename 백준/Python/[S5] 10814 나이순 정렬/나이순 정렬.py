import sys
input = sys.stdin.readline

N = int(input())
people = sorted([list(input().split()) for _ in range(N)], key = lambda x: int(x[0]))
for i in people:
    print(*i)
