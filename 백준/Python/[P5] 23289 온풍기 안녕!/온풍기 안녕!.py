from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 온풍기 바람 불기
# r, c, d: 시작 위치, 방향
def new_wind(r, c, d):
    # 방문 체크
    visited = [[0] * C for _ in range(R)]
    visited[r][c] = 1
    board[r][c] += 5

    # 탐색 위치, 온도를 담은 큐
    q = deque([(r, c, 5)])
    while q:
        r, c, k = q.popleft()

        # 1이 되면 더 이상 이동 불가
        if k == 1:
            break

        # 3 방향으로 이동
        for i, v in enumerate([(r + dr[d] + dr[(d - 1) % 4], c + dc[d] + dc[(d - 1) % 4]), (r + dr[d], c + dc[d]), (r + dr[d] + dr[(d + 1) % 4], c + dc[d] + dc[(d + 1) % 4])]):
            nr, nc = v

            # 범위 체크
            if not (0 <= nr < R and 0 <= nc < C):
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue

            # 벽 체크
            if i == 0 and (wall[(d + 2) % 4][nr][nc] or wall[(d - 1) % 4][r][c]):
                continue
            elif i == 1 and wall[d][r][c]:
                continue
            elif i == 2 and (wall[(d + 2) % 4][nr][nc] or wall[(d + 1) % 4][r][c]):
                continue

            # 이동
            board[nr][nc] += k - 1
            visited[nr][nc] = 1
            q.append((nr, nc, k - 1))

########################################################################################################3

# 온도 조절
def manipulate():
    # 변화하는 칸과 그 양
    change = defaultdict(int)

    # 모든 칸 탐색
    for r in range(R):
        for c in range(C):
            # 현재 칸 온도
            t1 = board[r][c]

            # 변화량
            total = 0

            # 사방 탐색
            for d in range(4):
                # 벽 체크
                if wall[d][r][c]:
                    continue

                nr, nc = r + dr[d], c + dc[d]

                # 범위 체크
                if not (0 <= nr < R and 0 <= nc < C):
                    continue

                # 현재 칸보다 낮은 경우
                t2 = board[nr][nc]
                if t2 < t1:
                    num = (t1 - t2) // 4
                    total += num
                    change[(nr, nc)] += num

            # 현재 칸의 감소량
            change[(r, c)] -= total

    # 변화하는 칸 탐색
    for k, v in change.items():
        r, c = k
        board[r][c] += v

########################################################################################################3

# 가장 바깥쪽 온도 -1
def decrease():
    # 첫 행, 마지막 행
    for c in range(C):
        if board[0][c]:
            board[0][c] -= 1
        if board[R - 1][c]:
            board[R - 1][c] -= 1

    # 첫 열, 마지막 열
    for r in range(1, R - 1):
        if board[r][0]:
            board[r][0] -= 1
        if board[r][C - 1]:
            board[r][C - 1] -= 1

########################################################################################################3

# 조사해야 하는 칸들의 온도 조사
def finish():
    # 조사해야 하는 칸
    for r, c in pos:
        # K 미만인 경우 미완료
        if board[r][c] < K:
            return 0

    # 모든 칸 K 이상
    return 1

########################################################################################################3

# 구사과가 먹는 초콜릿 개수 구하기
def get_cnt():
    # 구사과가 먹는 초콜릿 개수
    cnt = 0

    while True:
        # 온풍기 바람 불기
        for r, c, d in wind:
            new_wind(r, c, d)

        # 온도 조절
        manipulate()

        # 가장 바깥쪽 온도 -1
        decrease()

        # 초콜릭 먹기 (최대 100개)
        cnt += 1
        if cnt == 101:
            return cnt

        # 조사해야 하는 칸들의 온도 조사
        if finish():
            return cnt

########################################################################################################3

# 방 크기, 조사해야 하는 칸들의 기준 온도
R, C, K = map(int, input().split())

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 온풍기 바람 시작 위치와 방향
wind = []

# 온도를 조사해야 하는 칸
pos = []

for r in range(R):
    row = list(map(int, input().split()))
    for c, info in enumerate(row):
        if info == 1:
            wind.append((r, c + 1, 1))
        elif info == 2:
            wind.append((r, c - 1, 3))
        elif info == 3:
            wind.append((r - 1, c, 0))
        elif info == 4:
            wind.append((r + 1, c, 2))
        elif info == 5:
            pos.append((r, c))

# 각 칸의 온도
board = [[0] * C for _ in range(R)]

# 벽의 개수
W = int(input())

# 벽 정도
# wall[d][r][c] : (r, c)의 d방향에 벽 존재
wall = [[[0] * C for _ in range(R)] for _ in range(4)]
for _ in range(W):
    r, c, t = map(int, input().split())
    r -= 1
    c -= 1
    if t == 0:
        wall[0][r][c] = wall[2][r - 1][c] = 1
    else:
        wall[1][r][c] = wall[3][r][c + 1] = 1

# 구사과가 먹는 초콜릿 개수
print(get_cnt())