from collections import deque
import sys
input = sys.stdin.readline

# 현재 방향으로 이동했을 때의 위치와 미끌 시간 구하기
def get_pos(r, c, d):
    # 미끌 시간
    time = 0

    # 바위나 출구가 있을 때까지 미끄러지기
    while True:
        nr, nc = r + dr[d], c + dc[d]

        # 범위를 벗어난 경우
        if not (0 <= nr < H and 0 <= nc < W):
            return -1, -1, -1

        # 구멍이 있는 경우
        if board[nr][nc] == -100:
            return -1, -1, -1

        # 바위가 있는 경우
        if board[nr][nc] == -1:
            return r, c, time

        # 출구가 있는 경우
        if nr == er and nc == ec:
            return nr, nc, time

        # 이동
        time += board[nr][nc]
        r, c = nr, nc

############################################################################################################################

# 최단 탈출 시간 구하기
def get_time():
    # 위치, 미끌 시간, 이전 방향을 담은 큐
    q = deque([(sr, sc, 0, -1)])
    while q:
        # 위치, 미끌 시간, 이전 방향
        r, c, time, prev = q.popleft()

        # 저장된 시간보다 오래 걸린 경우 패스
        if time > min_time[r][c]:
            continue

        # 이동 방향
        for d in range(4):
            # 이전 이동 방향 패스
            if d == prev:
                continue

            # 현재 방향에 바위가 없는 경우 끝내기
            if d % 2 and not rock_row[r] and r != er:
                continue
            elif d % 2 == 0 and not rock_col[c] and c != ec:
                continue

            # 현재 방향으로 이동했을 때의 위치와 미끌 시간
            nr, nc, ntime = get_pos(r, c, d)

            # 미끄러졌을 때 구멍에 빠지거나 범위를 벗어나는 경우 현재 방향 불가
            if nr == -1:
                continue

            # 탈출한 경우 끝내기
            if nr == er and nc == ec:
                min_time[nr][nc] = min(min_time[nr][nc], time + ntime)
                continue

            # 저장된 시간보다 짧게 걸린 경우, 큐에 추가
            if time + ntime < min_time[nr][nc]:
                min_time[nr][nc] = min(min_time[nr][nc], time + ntime)
                q.append((nr, nc, time + ntime, d))

############################################################################################################################

# 얼음 미로 크기
W, H = map(int, input().split())

# 테라 위치, 출구 위치
sr = sc = er = ec = -1

# 미로 정보
board = []

# 각 행, 열별 바위 존재 여부
rock_row = [0] * H
rock_col = [0] * W

for i in range(H):
    row = list(map(lambda x: {'T': 100, 'R': -1, 'H': -100, 'E': 200}[x] if x.isalpha() else int(x), input().rstrip()))
    board.append(row)
    for j, info in enumerate(row):
        if info == 100:
            sr, sc = i, j
            board[i][j] = 0
        elif info == 200:
            er, ec = i, j
            board[i][j] = 0
        elif info == -1:
            rock_row[i] = 1
            rock_col[j] = 1

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 각 칸까지의 최소 미끌 시간
min_time = [[25000000] * W for _ in range(H)]
min_time[sr][sc] = 0

# 최단 탈출 시간 구하기
get_time()

# 탈출이 불가능한 경우
res = min_time[er][ec]
if res == 25000000:
    print(-1)
else:
    print(res)
