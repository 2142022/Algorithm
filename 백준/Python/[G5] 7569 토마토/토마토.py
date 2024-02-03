from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 모든 토마토가 익을 때까지 걸리는 최소 일수
def bfs(H, N, M, remain):
    # 육방 탐색용
    dh, dr, dc = (0, 0, 0, 0, -1, 1), (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0)

    while q:
        # 현재 토마토 위치
        h, r, c = q.popleft()

        # 현재 토마토가 익기까지 걸린 일 수
        day = tomatoes[h][r][c]

        # 육방 탐색
        for d in range(6):
            nh, nr, nc = h + dh[d], r + dr[d], c + dc[d]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and tomatoes[nh][nr][nc] == 0:
                remain -= 1
                # 모든 토마토가 익은 경우 (처음부터 토마토가 익은 날이 1로 돼있으므로 +1 하지 않음)
                if remain == 0:
                    return day
                tomatoes[nh][nr][nc] = day + 1
                q.append((nh, nr, nc))

    # 모든 토마토가 익지 못하는 경우
    return -1

##############################################################################################################

# 상자 크기, 수
M, N, H = map(int, input().split())

# 상자 정보
tomatoes = []
# 익은 토마토 위치를 담은 큐
q = deque()
# 익지 않은 토마토 개수
remain = 0
for k in range(H):
    box = []
    for i in range(N):
        row = list(map(int, input().split()))
        box.append(row)
        for j, num in enumerate(row):
            if num == 0:
                remain += 1
            elif num == 1:
                q.append((k, i, j))
    tomatoes.append(box)

# 이미 모든 토마토가 익어있는 경우
if remain == 0:
    print(0)

# 모든 토마토가 익을 때까지 걸리는 최소 일수
else:
    print(bfs(H, N, M, remain))

