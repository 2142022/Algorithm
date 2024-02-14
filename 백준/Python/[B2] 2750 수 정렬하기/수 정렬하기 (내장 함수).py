import sys
input = sys.stdin.readline

# 수 개수
N = int(input())

print(*sorted([int(input()) for _ in range(N)]), sep='\n')