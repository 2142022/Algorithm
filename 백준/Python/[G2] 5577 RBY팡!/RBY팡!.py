import sys
input = sys.stdin.readline

# a번째 공을 b번째 공의 색으로 바꿨을 때 남아있는 최소 공의 수 구하기
def change(a, b, balls):
    # 공의 색 바꾸기
    balls[a] = balls[b]

    # 탐색 시작 위치
    start = a

    # 소멸하는 공이 없을 때까지 반복
    while True:
        # 탐색하는 공의 색
        color = balls[start]

        # 소멸시킬 범위
        left, right = start, start

        # 아래 공 탐색
        for i in range(start, -1, -1):
            if balls[i] != color:
                break
            left = i

        # 위 공 탐색
        for i in range(start + 1, len(balls)):
            if balls[i] != color:
                break
            right = i

        # 4개 미만인 경우 소멸 불가
        if right - left + 1 < 4:
            break

        # 연속된 공 소멸
        balls = balls[:left] + balls[right + 1:]
        start = max(left - 1, 0)

        # 모두 소멸한 경우 끝내기
        if not balls:
            break

    return len(balls)

################################################################################

# 공의 수
N = int(input())

# 공의 색
balls = [int(input()) for _ in range(N)]

# 남아있는 공의 최솟값
M = N

# 공의 색을 하나씩 바꾸기
for i in range(N):
    # 현재 공을 양 옆의 공과 같은 색으로 바꾸기
    if i - 1 >= 0 and balls[i - 1] != balls[i]:
        M = min(M, change(i, i - 1, balls[:]))
    if i + 1 < N and balls[i + 1] != balls[i]:
        if i - 1 >= 0 and balls[i - 1] == balls[i + 1]:
            continue
        M = min(M, change(i, i + 1, balls[:]))

print(M)