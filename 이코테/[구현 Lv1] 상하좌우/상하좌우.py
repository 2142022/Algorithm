import sys

input = sys.stdin.readline

# 공간의 크기
N = int(input())

# 이동 계획
plan = list(input())

# 시작 위치: (1, 1)
r = c = 1

# 이동하기
for i in range(len(plan)):
    # 다음 위치
    nr = r
    nc = c

    # 상
    if plan[i] == 'U':
        nr -= 1
    # 하
    elif plan[i] == 'D':
        nr += 1
    # 좌
    elif plan[i] == 'L':
        nc -= 1
    # 우
    elif plan[i] == 'R':
        nc += 1

    # 공간을 벗어나지 않는 경우에만 이동
    if 0 < nr <= N and 0 < nc <= N:
        r = nr
        c = nc

# 출력: 최종 도착 지점
print(r, c)
