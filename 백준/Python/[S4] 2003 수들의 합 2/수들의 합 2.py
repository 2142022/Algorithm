import sys
input = sys.stdin.readline

# N: 수의 개수, M: 합이 될 수
N, M = map(int, input().split())

# 수열
A = list(map(int, input().split()))

# 연속된 수를 더해서 M이 될 수 있는 경우의 수
cnt = 0

# 연속된 수의 시작지점과 끝지점
start = end = 0

# 연속된 수의 합
sum_num = A[0]

# 끝 지점이 나올 때까지 반복
while end < N:
    # 현재 합이 M보다 작은 경우 끝 지점을 늘리기
    if sum_num < M:
        end += 1
        if end < N:
            sum_num += A[end]
    # 현재 합이 M인 경우 cnt, start, end 모두 +1
    elif sum_num == M:
        cnt += 1
        start += 1
        end += 1
        if end < N:
            sum_num += A[end] - A[start - 1]
    # 현재 합이 M보다 큰 경우 시작 지점 늘리기
    else:
        start += 1
        sum_num -= A[start - 1]

print(cnt)