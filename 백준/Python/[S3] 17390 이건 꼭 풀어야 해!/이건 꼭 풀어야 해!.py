import sys
input = sys.stdin.readline

# 수열 크기, 질문 개수
N, Q = map(int, input().split())

# 수열 (오름차순으로 정렬 후 누적합)
A = [0] + sorted(list(map(int, input().split())))
for i in range(1, N + 1):
    A[i] += A[i - 1]

# 질문
for _ in range(Q):
    # 더할 범위
    L, R = map(int, input().split())

    # L번째 수부터 R번째 수까지 더하기
    print(A[R] - A[L - 1])
