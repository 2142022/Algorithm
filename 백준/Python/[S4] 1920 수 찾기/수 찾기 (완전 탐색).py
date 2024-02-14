import sys
input = sys.stdin.readline

# 정수 개수
N = int(input())

# N개의 정수
nums = set(map(int, input().split()))

# 비교할 수의 개수
M = int(input())

# 비교할 수
find = list(map(int, input().split()))

# 하나씩 비교
for i in find:
    if i in nums:
        print(1)
    else:
        print(0)