import sys
input = sys.stdin.readline

# 가로 길이
N = int(input())

# 가로의 길이에 따른 경우의 수
cnt = [0] * (N + 1)

# 가로의 길이가 1일 때의 경우의 수는 1가지
# 가로의 길이가 2일 때의 경우의 수는 3가지
cnt[1] = 1
cnt[2] = 3

# 점화식: f(n) = f(n - 1) + 2f(n - 2)
# (n - 1 경우에서 2X1 바닥 이어붙이기)
# + (n - 2 경우에서 1X2 바닥 두 개 이어붙이기)
# + (n - 2 경우에서 2X2 바닥 이어붙이기)
# 문제: 796796으로 나눈 나머지 구하기
for i in range(3, N + 1):
    cnt[i] = (cnt[i - 1] + 2 * cnt[i - 2] ) % 796796

print(cnt[N])