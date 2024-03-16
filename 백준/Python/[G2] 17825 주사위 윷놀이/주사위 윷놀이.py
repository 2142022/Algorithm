import sys
input = sys.stdin.readline

# 한 개씩 이동시키기
# cnt: 이동 횟수
# score: 현재까지의 점수
def move(cnt, score):
    global max_score

    # 모두 이동시킨 경우 끝내기
    if cnt == 10:
        max_score = max(max_score, score)
        return

    # 모든 말이 도착한 경우 끝내기
    if pos[0] == pos[1] == pos[2] == pos[3] == -1:
        max_score = max(max_score, score)
        return

    # 현재 주사위 수
    num = dice[cnt]

    # 이동 시킬 말
    for i in range(4):
        # 현재 말의 위치
        p = pos[i]

        # 이미 도착한 말은 패스
        if p == -1:
            continue

        # 주사위 수만큼 이동
        np = p
        for j in range(num):
            if j == 0 and len(connect[p]) >= 2:
                np = connect[np][1]
            else:
                np = connect[np][0]

            # 목적지에 도착한 경우
            if np == -1:
                break

        # 이미 다른 말이 있는 경우 패스
        if np != -1 and np in pos:
            continue

        # 목적지에 도착한 경우
        if np == -1:
            pos[i] = np
            move(cnt + 1, score)
            pos[i] = p

        # 점수 갱신
        else:
            pos[i] = np
            move(cnt + 1, score + circles[np])
            pos[i] = p

    return

#########################################################################################################

# 주사위 번호
dice = list(map(int, input().split()))

# 경로
connect = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 24], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [-1], [22], [23], [26], [25], [26], [30], [28], [29], [26], [31], [20]]

# 각 칸의 점수
circles = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 25, 28, 27, 26, 30, 35]

# 말의 위치
pos = [0] * 4

# 최대 점수
max_score = 0

# 한 개씩 이동시키기
move(0, 0)

print(max_score)