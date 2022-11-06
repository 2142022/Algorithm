import sys
input = sys.stdin.readline

# 받아야 할 거스름돈
N = 1000 - int(input())

# 거스름돈으로 사용할 동전
coin = [500, 100, 50, 10, 5, 1]

# 동전의 개수
cnt = 0

# 값이 큰 동전부터 개수 구하기
for i in coin:
    cnt += N // i
    N %= i

print(cnt)