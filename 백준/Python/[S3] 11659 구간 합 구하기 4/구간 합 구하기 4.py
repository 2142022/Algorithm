import sys
input = sys.stdin.readline

# N: 수의 개수, M: 합을 구해야 하는 횟수
N, M = map(int, input().split())

# N개의 수
nums = list(map(int, input().split()))

# s[i]: nums[0]부터 nums[i]까지의 합
s = [0] * (N + 1)
s[1] = nums[0]
for i in range(2, N + 1):
    s[i] = s[i - 1] + nums[i - 1]

# M번 합 구하기
for _ in range(M):
    # num[i - 1]부터 nums[j - 1]까지의 합 구하기
    i, j = map(int, input().split())

    print(s[j] - s[i - 1])