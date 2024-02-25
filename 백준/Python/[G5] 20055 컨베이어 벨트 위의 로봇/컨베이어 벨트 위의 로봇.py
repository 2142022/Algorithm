import sys
input = sys.stdin.readline

# 컨베이터 벨트 한 줄의 크기, 종료 시 내구도가 0인 칸의 개수
N, K = map(int, input().split())

# 컨베이어 벨트의 총 길이
M = 2 * N

# 컨베이어 벨트
A = list(map(int, input().split()))

# 내구도가 0인 칸의 개수
cnt = 0

# 단계
level = 1

# 올리는 위치, 내리는 위치
up, down = 0, N - 1

# 로봇의 위치
robot = []

# 내구도가 0인 칸의 개수가 K개 이상이 되면 끝내기
while True:
    # 벨트 회전
    up = (up - 1) % M
    down = (down - 1) % M

    # 로봇 내리기
    if down in robot:
        robot.remove(down)

    # 내릴 로봇
    remove = -1

    # 로봇 이동
    for i, pos in enumerate(robot):
        # 다음 칸
        npos = (pos + 1) % M

        # 다음 칸의 내구도가 0이 아니거나 로봇이 없는 경우
        if A[npos] and (npos == down or npos not in robot):
            A[npos] -= 1
            robot[i] = npos

            if A[npos] == 0:
                cnt += 1

            # 내리는 위치에 도착한 경우 바로 내리기
            if npos == down:
                remove = i

    # 내릴 로봇이 있으면 내리기
    if remove != -1:
        robot.pop(remove)

    # 로봇 올리기
    if A[up] and up not in robot:
        A[up] -= 1
        if A[up] == 0:
            cnt += 1
        robot.append(up)

    if cnt >= K:
        break

    level += 1

print(level)
