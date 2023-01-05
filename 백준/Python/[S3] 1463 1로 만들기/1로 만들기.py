import sys
input = sys.stdin.readline

# 정수 N
N = int(input())

# 연산 횟수를 기록하는 리스트
cnt = [2147483647] * (N + 1)
cnt[0] = cnt[1] = 0

# 1부터 N까지 +1, x2, x3하기
for i in range(1, N + 1):
    # +1
    if i + 1 <= N:
        cnt[i + 1] = min(cnt[i] + 1, cnt[i + 1])

    # x2
    if i * 2 <= N:
        cnt[i * 2] = min(cnt[i] + 1, cnt[i * 2])

    # x3
    if i * 3 <= N:
        cnt[i * 3] = min(cnt[i] + 1, cnt[i * 3])

print(cnt[N])