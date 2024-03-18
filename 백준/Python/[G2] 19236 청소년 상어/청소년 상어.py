import sys
input = sys.stdin.readline

# 물고기 & 상어 이동
def eat(board, fish, score):
    global max_score

    # 더 이상 먹을 수 있는 물고기가 없는 경우 끝내기
    if score == 136:
        max_score = 136
        return 1

    # 물고기 이동
    for num in range(1, 17):
        # 이미 먹힌 경우 패스
        if not fish[num]:
            continue

        # 현재 위치, 방향
        r, c, d = fish[num]

        # 최대 8번 회전
        for _ in range(8):
            # 다음 위치
            nr, nc = r + dr[d], c + dc[d]

            # 범위를 벗어나거나 상어가 있는 경우 회전
            if not (0 <= nr < 4 and 0 <= nc < 4) or board[nr][nc] == 0:
                d = (d + 1) % 8
                fish[num][2] = d
                continue

            # 빈 칸인 경우 이동
            if board[nr][nc] == -1:
                board[nr][nc], board[r][c] = num, -1
                fish[num] = [nr, nc, d]
                break

            # 다른 물고기가 있는 경우, 자리 바꾸기
            elif board[nr][nc] > 0:
                other = board[nr][nc]
                board[nr][nc], board[r][c] = num, other
                fish[other][:2], fish[num][:2] = fish[num][:2], fish[other][:2]
                break

    # 상어 이동
    r, c, d = fish[0]

    # 현재 상어가 먹을 수 있는 물고기 개수
    cnt = 0

    # 이동 위치
    nr, nc = r + dr[d], c + dc[d]
    while 0 <= nr < 4 and 0 <= nc < 4:
        # 현재 물고기
        num = board[nr][nc]

        # 물고기가 없는 경우 패스
        if num == -1:
            nr += dr[d]
            nc += dc[d]
            continue

        # 현재 물고기 먹기
        cnt += 1
        max_score = max(max_score, score + num)
        board_copy = [b[:] for b in board]
        fish_copy = [f[:] for f in fish]
        board_copy[r][c], board_copy[nr][nc] = -1, 0
        fish_copy[num], fish_copy[0] = [], fish_copy[num][:]

        # 다음 물고기 먹기
        if eat(board_copy, fish_copy, score + num):
            return 1

        # 한 칸 더 이동
        nr += dr[d]
        nc += dc[d]

    # 한 마리도 먹지 못한 경우 끝내기
    if cnt == 0:
        return 0

################################################################################

# 각 칸에 있는 물고기 번호
board = [[0] * 4 for _ in range(4)]

# 각 물고기의 위치와 방향
fish = [list() for _ in range(17)]

# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값
max_score = 0

# 입력받기
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        # 물고기 번호, 방향
        num, d = row[2 * j], row[2 * j + 1]
        d -= 1

        # (0, 0)은 상어
        if i == j == 0:
            max_score += num
            num = 0

        # 보드에 저장
        board[i][j] = num
        fish[num] = [i, j, d]

# 8방 탐색용
dr, dc = (-1, -1, 0, 1, 1, 1, 0, -1), (0, -1, -1, -1, 0, 1, 1, 1)

# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값 구하기
eat([b[:] for b in board], [f[:] for f in fish], max_score)
print(max_score)