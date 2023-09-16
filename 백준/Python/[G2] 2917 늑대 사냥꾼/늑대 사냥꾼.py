from collections import deque
import sys, heapq
input = sys.stdin.readline

# 숲 크기 N X M
N, M = map(int, input().split())

# 숲 정보
forest = []
# 나무 위치
tree = []
# 현우 위치
sr = sc = 0
# 오두막 위치
fr = fc = 0
for i in range(N):
    info = list(input().rstrip())
    forest.append(info)
    for j in range(M):
        if info[j] == '+':
            tree.append((i, j))
        elif info[j] == 'V':
            sr, sc = i, j
        elif info[j] == 'J':
            fr, fc = i, j

# 사방 탐색용
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 각 칸에서 나무까지의 최소 거리
# BFS로 구하지 않고 이중 for문으로 하는 모든 칸 탐색하면 시간 초과
dist = [[-1] * M for _ in range(N)]
q = deque()
for i, j in tree:
    q.append((i, j, 0))
    dist[i][j] = 0
while q:
    r, c, d = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if dist[nr][nc] != -1:
            continue
        dist[nr][nc] = d + 1
        q.append((nr, nc, d + 1))

# 방문 체크
visited = [[0] * M for _ in range(N)]

# 현재 경로에서 나무까지의 최소 거리와 현재 위치를 담은 최소 힙
h = []
heapq.heappush(h, (-dist[sr][sc], sr, sc))

# 경로 탐색
while h:
    # 현재 경로에서 나무까지의 최소 거리, 현재 위치
    d, r, c = heapq.heappop(h)

    # 방문 체크
    if visited[r][c]:
        continue
    visited[r][c] = 1

    # 오두막에 도착한 경우 끝내기
    if r == fr and c == fc:
        print(-d)
        break

    # 사방 탐색
    for i in range(4):
        # 다음 위치
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위를 벗어난 경우 패스
        if not (0 <= nr < N and 0 <= nc < M):
            continue

        # 이미 방문한 곳은 패스
        if visited[nr][nc]:
            continue

        # 다음 위치 힙에 넣기
        heapq.heappush(h, (-min(dist[nr][nc], -d), nr, nc))