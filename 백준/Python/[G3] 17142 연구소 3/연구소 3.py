from collections import deque
import sys
input = sys.stdin.readline

# pos에 있는 바이러스를 활성화시켰을 때, 모든 빈 칸에 바이러스를 퍼뜨리는데 걸리는 최소 시간과 남은 빈 칸 개수 구하기
def spread(pos, empty):
    time = 0
    board_copy = [b[:] for b in board]

    # 탐색 위치와 현재 시간을 담은 큐
    q = deque()

    # 탐색 위치에 있는 바이러스 모두 활성화
    for r, c in pos:
        board_copy[r][c] = 0
        q.append((r, c, 0))

    while q:
        # 위치
        r, c, t = q.popleft()

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 벽 패스
            if board_copy[nr][nc] == -1:
                continue

            # 빈 칸 큐에 담기
            elif board_copy[nr][nc] == -100:
                board_copy[nr][nc] = t + 1
                empty -= 1
                q.append((nr, nc, t + 1))
                time = t + 1

            # 비활성화 바이러스 활성화
            elif board_copy[nr][nc] == -2:
                q.append((nr, nc, t + 1))

    return time, empty

#######################################################################################################################

# 활성 바이러스 하나 선택하기
# cnt: 활성화시킨 바이러스 수
def select(cnt):
    global min_time

    # M개의 바이러스 활성화
    if cnt == M:
        virus_pos = [pos[i] for i in virus]
        time, empty = spread(virus_pos, total_empty)
        if empty == 0:
            min_time = min(min_time, time)
            if min_time == min_time_all:
                return 1
        return 0

    virus_pos = [pos[i] for i in virus]
    time, empty = spread(virus_pos, total_empty)
    if empty == 0 and min_time == min_time_all:
        return 1

    # 활성화시킬 바이러스
    start = virus[-1] + 1 if virus else 0
    for i in range(start, len(pos) - M + cnt + 1):
        virus.append(i)
        # 다음 바이러스 선택
        if select(cnt + 1):
            return 1
        virus.pop()

    return 0

#######################################################################################################################

# 연구소 크기, 놓을 수 있는 바이러스 개수
N, M = map(int, input().split())

# 연구소 상태 (빈 칸: -100, 벽: -1, -2: 비활성 바이러스, 0: 활성 바이러스, 1 이상: 시간)
board = []
# 모든 바이러스의 위치
pos = []
# 모든 빈 칸 개수
total_empty = 0
for i in range(N):
    row = list(map(lambda x: {0: -100, 1: -1, 2: -2}[int(x)], input().split()))
    board.append(row)
    for j, info in enumerate(row):
        if info == -2:
            pos.append((i, j))
        elif info == -100:
            total_empty += 1

# 모든 바이러스를 활성화시켰을 때, 모든 빈 칸에 바이러스를 퍼뜨리는데 걸리는 최소 시간
min_time_all, empty = spread(pos, total_empty)

# 원래 빈 칸이 없는 경우
if total_empty == 0:
    print(0)

# 모든 빈 칸에 바이러스가 퍼지지 않는 경우 -1
elif empty != 0:
    print(-1)

# 모든 바이러스를 활성화할 수 있는 경우
elif len(pos) == M:
    print(min_time_all)

# 활성 바이러스 하나씩 선택하기
else:
    # 모든 칸에 바이러스가 퍼지는 최소 시간
    min_time = N * N

    # 활성화시킬 바이러스
    virus = []
    select(0)

    if min_time == N * N:
        print(-1)
    else:
        print(min_time)