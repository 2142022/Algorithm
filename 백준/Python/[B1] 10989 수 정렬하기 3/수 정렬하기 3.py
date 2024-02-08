import sys
input = sys.stdin.readline

# 수의 개수
N = int(input())

# 각 숫자의 개수
cnt = [0] * 10001
for _ in range(N):
    cnt[int(input())] += 1

# 개수만큼 출력
for num, c in enumerate(cnt):
    if c:
        for _ in range(c):
            print(num)