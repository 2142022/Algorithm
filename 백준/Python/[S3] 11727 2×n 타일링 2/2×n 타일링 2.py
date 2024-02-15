import sys
input = sys.stdin.readline

# 직사각형 가로 길이
n = int(input())

# 나눌 수
m = 10007

# cnt[i]: 2Xi 크기의 직사각형을 채우는 방법의 수
cnt = [0] * (n + 1)
cnt[1] = 1
if n > 1:
    cnt[2] = 3
for i in range(3, n + 1):
    # i-1까지 채웠을 때, 2x1 직사각형 넣는 방법
    # + i-2까지 채웠을 때, 2x1 직사각형 2개를 넣거나 2x2 직사각형 1개를 넣는 방법
    cnt[i] = (cnt[i - 1] + 2 * cnt[i - 2]) % m

print(cnt[n])