import sys
input = sys.stdin.readline

# 사람 수, 제거할 사람 번호
N, K = map(int, input().split())

# 마지막으로 뽑은 사람의 번호
last = 0
for i in range(1, N + 1):
    # 점화식: f(N, K) = (f(N - 1, K) + K) mod N
    last = (last + K) % i

# 사람 번호는 1부터 시작하므로 +1
print(last + 1)