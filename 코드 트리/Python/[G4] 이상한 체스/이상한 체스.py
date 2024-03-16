import sys
input = sys.stdin.readline

# i번째 말 이동하기
# v: 현재까지 말들이 탐색한 곳 방문 체크
# cnt: 비어있음에도 탐색하지 않는 곳의 개수
def move(i, v, cnt):
    global min_cnt

    # 모든 말을 다 탐색한 경우
    if i == len(pos):
        min_cnt = min(min_cnt, cnt)
        # 비어있는 칸이 없는 경우, 완전히 끝내기
        if min_cnt == 0:
            return 1
        return 0

    # 현재 말의 위치, 종류
    r, c, t = pos[i]

    # 현재 위치도 탐색
    v |= 1 << (M * r + c)
    cnt -= 1

    # 현재 말의 탐색방향
    for sd in SD[t]:
        # 현재 말을 탐색하고 난 후의 방문 체크, 비어있는 칸의 개수
        nv = v
        ncnt = cnt

        # 탐색 방향
        for d in sd:
            nr, nc = r + dr[d], c + dc[d]
            while 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 6:
                # 비어있는 경우 방문 체크
                if board[nr][nc] == 0 and not nv & 1 << (M * nr + nc):
                    nv |= 1 << (M * nr + nc)
                    ncnt -= 1
                nr += dr[d]
                nc += dc[d]

        # 다음 말 탐색
        if move(i + 1, nv, ncnt):
            return 1

    return 0

##################################################################################

# 체스판 크기
N, M = map(int, input().split())

# 체스판
board = []

# 말의 위치와 번호
pos = []

# 비어있는 칸의 개수
empty = N * M

# 입력받기
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j, info in enumerate(row):
        if 1 <= info <= 5:
            pos.append((i, j, info))
        elif info == 6:
            empty -= 1

# 사방 탐색용 (상하좌우)
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 말별 탐색 방향
SD = {1: [(0,), (1,), (2,), (3,)],
      2: [(0, 1), (2, 3)],
      3: [(0, 3), (3, 1), (1, 2), (2, 0)],
      4: [(0, 2, 3), (3, 0, 1), (1, 2, 3), (2, 0, 1)],
      5: [(0, 1, 2, 3)]}

# 비어있음에도 갈 수 없는 체스판의 최소 영역
min_cnt = empty

# 말 하나씩 탐색하기
move(0, 0, empty)

print(min_cnt)