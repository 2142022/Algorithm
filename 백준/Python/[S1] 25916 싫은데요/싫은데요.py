import sys
input = sys.stdin.readline

# 구멍 수, 햄스터 부피
N, M = map(int, input().split())

# 구멍의 크기 (누적합)
A = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    A[i] += A[i - 1]

# 막을 수 있는 최대 부피
volume = 0

# 막는 구멍의 시작, 마지막
start, end = 0, 1

# 구멍 하나씩 탐색
while end <= N:
    # 현재 구멍을 막았을 때 M을 초과하는 경우 start를 뒤로 보내기
    while A[end] - A[start] > M:
        start += 1

    # 현재 구멍 막기
    volume = max(volume, A[end] - A[start])
    end += 1

print(volume)