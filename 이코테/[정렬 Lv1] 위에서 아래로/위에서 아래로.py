import sys
input = sys.stdin.readline

# 수의 개수
N = int(input())

# N개의 수 입력받기
nums = []
for i in range(N):
    nums.append(int(input()))

# 내림차순 정렬하기
nums.sort(reverse=True)

# 출력하기
for i in nums:
    print(i, end=' ')