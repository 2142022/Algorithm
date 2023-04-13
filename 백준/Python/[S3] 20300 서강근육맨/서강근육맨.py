import sys
input = sys.stdin.readline

# 운동기구의 개수
N = int(input())

# 각 운동기구의 근손실 정도
t = list(map(int, input().split()))
# 오름차순 정렬
t.sort()

# 최소 근손실 기준
M = 0

# 처음과 마지막을 더하기
# 운동 기구 개수가 홀수인 경우 마지막은 제외하고 생각하기
for i in range(N // 2):
    if N % 2 == 0:
        M = max(M, t[i] + t[N - 1 - i])
    else:
        M = max(M, t[i] + t[N - 2 - i])

# 운동 기구 개수가 홀수인 경우, 마지막 하나만 따로 비교하기
if N % 2 == 1:
    M = max(M, t[N - 1])

print(M)