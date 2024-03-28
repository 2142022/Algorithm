from collections import defaultdict
import sys
input = sys.stdin.readline

# 연쇄 이동
# (sr, sc): 산타의 충돌 위치
# (dr, dc): 이동 방향
# cnt: 충돌한 후 이동 칸 수
def push(sr, sc, dr, dc, cnt):
    # 충돌한 산타
    num = board[sr][sc]

    # 산타가 충돌 후, 이동한 위치
    r, c = sr + dr * cnt, sc + dc * cnt

    # 범위 체크
    if not (0 <= r < N and 0 <= c < N):
        santa.pop(num)
        board[sr][sc] = 0
        return

    # 그 위치에 산타가 없는 경우, 현재 산타만 이동
    if not board[r][c]:
        board[sr][sc] = 0
        board[r][c] = num
        santa[num][:2] = [r, c]
        return

    # 밀려나는 산타들의 위치
    else:
        pos = [(r, c)]
        while True:
            r += dr
            c += dc

            # 범위 체크
            if not (0 <= r < N and 0 <= c < N):
                break

            # 빈 칸 체크
            if not board[r][c]:
                break

            pos.append((r, c))

        # 끝에서부터 한 명씩 밀기
        for i in range(len(pos) - 1, -1, -1):
            r, c = pos[i]
            nr, nc = r + dr, c + dc
            s = board[r][c]

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                santa.pop(s)
                board[r][c] = 0
                continue

            # 이동
            board[nr][nc] = s
            santa[s][:2] = [nr, nc]

        # 처음 산타 이동
        board[r][c] = num
        board[sr][sc] = 0
        santa[num][:2] = [r, c]

##################################################################################################################################################

# 루돌프 이동
def moveR():
    global rr, rc

    # 가장 가까운 산타의 위치
    sr, sc = sorted([(r, c) for r, c, t in santa.values()], key=lambda x: ((rr - x[0]) ** 2 + (rc - x[1]) ** 2, -x[0], -x[1]))[0]

    # 루돌프 이동 방향
    dr, dc = sorted(eight, key = lambda x: (rr + x[0] - sr) ** 2 + (rc + x[1] - sc) ** 2)[0]

    # 루돌프 이동 위치
    nr, nc = rr + dr, rc + dc

    # 산타와 충돌
    num = board[nr][nc]
    if num:
        # 산타 기절
        santa[num][2] = R + 1

        # 산타 점수 갱신
        score[num] += C

        # 연쇄 이동
        push(nr, nc, dr, dc, C)

    # 루돌프 이동
    rr, rc = nr, nc

##################################################################################################################################################

# 산타 이동
def moveS():
    # 산타 1번부터 순서대로 이동
    for num, info in sorted(list(santa.items())):
        # 이미 탈락한 경우 패스
        if num not in santa:
            continue

        r, c, t = info

        # 기절 상태인 경우 패스
        if R <= t:
            continue

        # 루돌프에게 가까워지는 방향 순서
        for dr, dc in sorted(four[:] + [(0, 0)], key = lambda x: (r + x[0] - rr) ** 2 + (c + x[1] - rc) ** 2):
            # 이동 위치
            nr, nc = r + dr, c + dc

            # 가까워지는 방향이 없는 경우
            if (nr, nc) == (r, c):
                break

            # 범위 밖인 경우 패스
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 다른 산타가 있는 경우 패스
            if board[nr][nc]:
                continue

            # 이동
            board[r][c] = 0
            board[nr][nc] = num
            santa[num][:2] = [nr, nc]

            # 루돌프와 충돌
            if (nr, nc) == (rr, rc):
                # 산타 기절
                santa[num][2] = R + 1

                # 산타 점수 갱신
                score[num] += D

                # 연쇄 이동
                push(nr, nc, -dr, -dc, D)

            break

##################################################################################################################################################

# 게임판 크기, 게임 턴 수, 산타 수, 루돌프 힘, 산타 힘
N, M, P, C, D = map(int, input().split())

# 루돌프 위치
rr, rc = map(lambda x: int(x) - 1, input().split())

# 게임판 (산타 번호)
board = [[0] * N for _ in range(N)]

# 산타 위치, 기절할 턴
santa = defaultdict(list)
for _ in range(P):
    num, r, c = map(int, input().split())
    board[r - 1][c - 1] = num
    santa[num] = [r - 1, c - 1, 0]

# 산타 점수
score = [0] * (P + 1)

# 8방 탐색
eight = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# 4방 탐색 (상우하좌)
four = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 게임 턴
for R in range(1, M + 1):
    # 루돌프 이동
    moveR()

    # 산타가 없는 경우 끝내기
    if not santa:
        break

    # 산타 이동
    moveS()

    # 산타가 없는 경우 끝내기
    if not santa:
        break

    # 살아있는 산타 점수 +1
    for num in santa:
        score[num] += 1

print(*score[1:])