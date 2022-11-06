import sys
input = sys.stdin.readline

# 손님에게 거슬러 줘야 할 돈
N = int(input())

# 거스름돈으로 사용할 동전
coin = [500, 100, 50, 10]

# 동전의 개수
cnt = 0

# 값이 큰 동전부터 개수 구하기
for i in coin:
    cnt += N // i
    N %= i

print(cnt)