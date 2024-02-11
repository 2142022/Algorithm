import sys
input = sys.stdin.readline

# 정수
N = int(input())

# 각 수를 만드는데 걸리는 횟수
cnt = [i - 1 for i in range(N + 1)]
for i in range(1, N + 1):
    # +1
    if i + 1 <= N:
        cnt[i + 1] = min(cnt[i + 1], cnt[i] + 1)

    # x2
    if 2 * i <= N:
        cnt[2 * i] = min(cnt[2 * i], cnt[i] + 1)

    # x3
    if 3 * i <= N:
        cnt[3 * i] = min(cnt[3 * i], cnt[i] + 1)

print(cnt[N])