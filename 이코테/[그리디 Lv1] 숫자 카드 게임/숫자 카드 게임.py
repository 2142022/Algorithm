import sys
input = sys.stdin.readline

# N: 행의 개수, M: 열의 개수
N, M = map(int, input().split())

# 가장 큰 숫자
max_num = 0

# 각 행마다 가장 작은 숫자 구하기
for i in range(N):
    card = list(map(int, input().split()))

    # 행의 가장 작은 숫자와 현재까지 구한 가장 큰 숫자 비교하기
    max_num = max(min(card), max_num)

print(max_num)