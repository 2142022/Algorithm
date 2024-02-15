import sys
input = sys.stdin.readline

# 정수
N = int(input())

# cnt[i]: 1을 i로 만드는데 필요한 최소 연산 수
cnt = [N] * (N + 1)
cnt[1] = 0
for i in range(1, N + 1):
    # +1, x2, x3
    for ni in (i + 1, i * 2, i * 3):
        if ni <= N:
            cnt[ni] = min(cnt[ni], cnt[i] + 1)

print(cnt[N])