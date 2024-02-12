import sys
input = sys.stdin.readline

# 강의 수, 블루레이 수
N, M = map(int, input().split())

# 강의 시간
time = list(map(int, input().split()))

# 최소 블루레이 크기
min_size = 10000 * N

# 블루레이 크기 범위
left, right = max(time), sum(time)
while left <= right:
    # 블루레이 크기
    size = (left + right) // 2

    # 블루레이 개수
    cnt = 1
    # 하나의 블루레이 크기
    s = 0
    for t in time:
        # size가 될 때까지 하나의 블루레이에 담기
        if s + t > size:
            s = 0
            cnt += 1
        s += t

    # 원하는 블루레이 개수보다 많다면 블루레이 크기 늘리기
    if cnt > M:
        left = size + 1
    else:
        min_size = size
        right = size - 1

print(min_size)