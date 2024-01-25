import sys
input = sys.stdin.readline

# 골목길 길이
N = int(input())

# 'WE'를 기준으로 구간이 나눠짐
print(input().rstrip().count('WE') + 1)
