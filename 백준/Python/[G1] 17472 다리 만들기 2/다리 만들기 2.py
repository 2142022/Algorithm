from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# (i, j)부터 시작되는 섬 num으로 체크하기
def find_island(i, j, num):
    board[i][j] = num

    # 탐색 위치를 담은 큐
    q = deque([(i, j)])
    while q:
        r, c = q.popleft()

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 땅 체크
            if board[nr][nc] == -1:
                board[nr][nc] = num
                q.append((nr, nc))

###############################################################################

# 두 섬을 연결할 수 있는 모든 다리 찾기
def find_bridge():
    for i in range(N):
        j = 1
        while j < M:
            # 땅 패스
            while j < M and board[i][j]:
                j += 1

            # 바다인 경우 다리 길이 세기
            d = 0
            while j + d < M and board[i][j + d] == 0:
                d += 1

            # 다리인 경우
            if j + d < M and d >= 2:
                island1, island2 = board[i][j - 1], board[i][j + d]
                if island1 and island2 and island1 != island2:
                    heappush(h, (d, island1, island2))
            j += d

    for j in range(M):
        i = 1
        while i < N:
            # 땅 패스
            while i < N and board[i][j]:
                i += 1

            # 바다인 경우 다리 길이 세기
            d = 0
            while i + d < N and board[i + d][j] == 0:
                d += 1

            # 다리인 경우
            if i + d < N and d >= 2:
                island1, island2 = board[i - 1][j], board[i + d][j]
                if island1 and island2 and island1 != island2:
                    heappush(h, (d, island1, island2))
            i += d

###############################################################################

# 섬 x와 연결된 섬들 중 가장 번호가 작은 섬
def find_idx(x):
    if min_idx[x] != x:
        min_idx[x] = find_idx(min_idx[x])
    return min_idx[x]

###############################################################################

# 두 섬 i1, i2가 아직 연결이 안된 경우 연결
def connect(i1, i2):
    i1 = find_idx(i1)
    i2 = find_idx(i2)

    if i1 < i2:
        min_idx[i2] = i1
        return 1
    elif i1 > i2:
        min_idx[i1] = i2
        return 1
    return 0

###############################################################################

# 지도 크기
N, M = map(int, input().split())

# 지도
board = [list(map(lambda x: -int(x), input().split())) for _ in range(N)]

# 섬 나누기
island_cnt = 1
for i in range(N):
    for j in range(M):
        # 섬 시작점
        if board[i][j] == -1:
            find_island(i, j, island_cnt)
            island_cnt += 1

# 모든 다리 정보를 담은 최소 힙 (다리 길이, 연결되는 두 섬)
h = []
find_bridge()

# 연결된 섬 중 가장 작은 섬
min_idx = [i for i in range(island_cnt)]

# 최소 다리 길이
total = 0

# 섬 연결하기
connect_cnt = 0
while h:
    # 현재 연결할 수 있는 가장 짧은 다리와 두 섬
    l, island1, island2 = heappop(h)

    # 아직 연결이 안된 경우 연결
    if connect(island1, island2):
        connect_cnt += 1
        total += l

        # 모두 연결된 경우 끝내기
        if connect_cnt == island_cnt - 2:
            break

# 모든 섬을 연결 불가능한 경우
if connect_cnt != island_cnt - 2:
    print(-1)
else:
    print(total)