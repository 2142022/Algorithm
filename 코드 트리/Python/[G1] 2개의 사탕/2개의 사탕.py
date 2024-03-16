import sys
input = sys.stdin.readline

# 이동할 수 있을 때까지 이동하기
# d: 이동 방향
# pos: 이동하는 사탕의 위치
# other: 다른 사탕의 위치
def check(d, pos, other):
    # 이동할 사탕의 위치
    r, c = divmod(pos, M)
    # 다른 사탕의 위치
    pr, pc = divmod(other, M)

    # 이동
    while True:
        nr, nc = r + dr[d], c + dc[d]

        # 장애물인 경우
        if board[nr][nc] == -1:
            return 0, M * r + c

        # 다른 사탕이 있는 경우
        if (nr, nc) == (pr, pc):
            return 0, M * r + c

        # 탈출
        if board[nr][nc] == 1:
            return 1, M * nr + nc

        # 이동
        r, c = nr, nc

###########################################################################################################

# d 방향으로 기울였을 때, 이동 가능 여부와 이동 후의 사탕들의 위치 구하기
def escape(d, red, blue):
    # 탈출 여부
    finish = 0

    # 파란색 사탕 이동
    flag, blue = check(d, blue, red)
    if flag:
        return -1, -1, -1

    # 빨간색 사탕 이동
    flag, red = check(d, red, blue)
    if flag:
        finish = 1
        red = -1

    # 파란색 사탕 이동
    flag, blue = check(d, blue, red)
    if flag:
        return -1, -1, -1

    return finish, red, blue

###########################################################################################################

# 기울이기
# cnt: 기울인 횟수
# red: 빨간 사탕 위치
# blue: 파란 사탕 위치
# pd: 직전 방향
def move(cnt, red, blue, pd):
    global min_cnt

    # 10번 모두 기울인 경우
    if cnt == 10:
        return 0

    # 최소 횟수 이상 기울인 경우 패스
    if cnt + 1 >= min_cnt:
        return 0

    # 기울일 방향
    for d in range(4):
        #직전 방향은 패스
        if d == pd:
            continue

        # 이동 가능 여부와 이동 후의 사탕들의 위치
        possible, nred, nblue = escape(d, red, blue)

        # 이동 불가
        if possible == -1:
            continue

        # 탈출
        if possible == 1:
            min_cnt = min(min_cnt, cnt + 1)
            if min_cnt == 1:
                return 1
            return 0

        # 이동 완료
        if move(cnt + 1, nred, nblue, d):
            return 1

###########################################################################################################

# 상자 크기
N, M = map(int, input().split())

# 상자 정보
board = []

# 출구, 빨간 사탕, 파란 사탕 위치
er = ec = rr = rc = br = bc = -1
for i in range(N):
    row = list(map(lambda x: {'.': 0, '#': -1, 'R': 10, 'B': 20, 'O': 1}[x], input().rstrip()))
    board.append(row)
    for j, info in enumerate(row):
        if info == 10:
            board[i][j] = 0
            rr, rc = i, j
        elif info == 20:
            board[i][j] = 0
            br, bc = i, j
        elif info == 1:
            er, ec = i, j

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 사탕을 빼내는 최소 횟수
min_cnt = 11

# 기울이기
move(0, M * rr + rc, M * br + bc, -1)

# 탈출 불가
if min_cnt == 11:
    print(-1)
else:
    print(min_cnt)