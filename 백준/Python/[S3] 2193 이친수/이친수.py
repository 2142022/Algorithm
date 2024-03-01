import sys
input = sys.stdin.readline

# 자릿수
N = int(input())

# N자릿수 이친수 개수: 피보나치 수열과 동일
cnt = [0] * (N + 1)
cnt[1] = 1
for i in range(2, N + 1):
    cnt[i] = cnt[i - 1] + cnt[i - 2]

print(cnt[N])