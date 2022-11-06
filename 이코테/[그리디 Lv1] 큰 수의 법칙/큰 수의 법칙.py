import sys
input = sys.stdin.readline

# N: 배열의 크기, M: 숫자가 더해지는 횟수, K: 배열의 특정 인덱스 값이 최대로 더해질 수 있는 횟수
N, M, K = map(int, input().split())

# N개의 자연수
num = list(map(int, input().split()))

# 정렬하여 가장 큰 자연수와 두 번째로 큰 자연수 구하기
num.sort()
max1 = num[-1]
max2 = num[-2]

# 숫자 M개의 총합
total = 0

# M개의 숫자 더하기
for i in range(M):
    # (K+1)번 째에는 max2를 더하고 나머지는 max1 더하기
    if i % (K + 1) != K:
        total += max1
    else:
        total += max2

print(total)