from collections import defaultdict
import sys
input = sys.stdin.readline

# i번째 말 이동하기
def move(i):
    # 현재 말의 위치, 방향
    r, c, d = pos[i]

    # 이동하려는 칸
    nr, nc = r + dr[d], c + dc[d]

    # 현재 말이 높이
    h = board[N * r + c].index(i)

    # 이동하는 말
    idxs = board[N * r + c][h:]

    # 현재칸에 남는 말들
    board[N * r + c] = board[N * r + c][:h]

    # 이동하려는 칸이 빨간색인 경우, 거꾸로
    if colors[nr][nc] == 1:
        idxs.reverse()

    # 이동
    board[N * nr + nc] += idxs
    for j in idxs:
        pos[j][0] = nr
        pos[j][1] = nc

    # 말이 4개 이상 있는 경우 끝내기
    if len(board[N * nr + nc]) >= 4:
        return 1
    return 0

########################################################################

# 게임 진행
def play():
    # 최대 1000번 진행
    for time in range(1, 1001):
        # 말
        for i in range(K):
            # 말의 위치와 방향
            r, c, d = pos[i]

            # 이동하려는 칸
            nr, nc = r + dr[d], c + dc[d]

            # 범위를 벗어나거나 파란색인 경우, 방향 바꾸기
            if not (0 <= nr < N and 0 <= nc < N) or colors[nr][nc] == 2:
                d = (d + 2) % 4
                pos[i][2] = d

                # 그래도 범위를 벗어나거나 파란색인 경우 패스
                nr, nc = r + dr[d], c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if colors[nr][nc] == 2:
                    continue

                # 이동하기
                if move(i):
                    return time

            # 흰색 & 빨간색
            else:
                if move(i):
                    return time

    # 게임이 끝나지 않는 경우
    else:
        return -1

########################################################################

# 체스판 크기, 말 개수
N, K = map(int, input().split())

# 체스판 (각 칸의 색)
colors = [list(map(int, input().split())) for _ in range(N)]

# 각 칸에 있는 말들의 번호
board = defaultdict(list)

# 말들의 위치와 방향
pos = []
for i in range(K):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    d = {1: 1, 2: 3, 3: 0, 4: 2}[d]
    pos.append([r, c, d])
    board[N * r + c].append(i)

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 게임이 종료되는 턴 구하기
print(play())