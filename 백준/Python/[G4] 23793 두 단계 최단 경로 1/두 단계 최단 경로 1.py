from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# x에서부터 y까지 갈 수 있는 최단 거리
# impossible: 갈 수 없는 정점
def dijkstra(x, y, impossible):
    global N

    # x에서부터 각 정점까지 갈 수 있는 최단 거리
    dist = [sys.maxsize] * (N + 1)
    dist[x] = 0

    # 현재 정점, 현재까지의 거리를 담은 큐
    q = deque([(x, 0)])
    while q:
        # 현재 정점, 현재까지의 거리
        u, d = q.popleft()

        # 기존 최단 거리보다 큰 경우 패스
        if d > dist[u]:
            continue

        # 연결된 정점 탐색
        for v, w in connect[u]:
            # 갈 수 없는 정점(Y)라면 패스
            if v == impossible:
                continue

            # 최단 거리 갱신
            if d + w < dist[v]:
                dist[v] = d + w
                q.append((v, d + w))

    # y까지 가는 경로가 없는 경우
    if dist[y] == sys.maxsize:
        return -1
    else:
        return dist[y]

###########################################################

# 정점 수, 간선 수
N, M = map(int, input().split())

# 간선 정보
connect = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    connect[u].append((v, w))

# X, Y, Z
x, y, z = map(int, input().split())

# X에서 Y로 갈 수 있는 최단 거리
xy = dijkstra(x, y, -1)
# Y에서 Z로 갈 수 있는 최단 거리
yz = dijkstra(y, z, -1)
# X에서 Y를 거치지 않고 Z로 갈 수 있는 최단 거리
connect.pop(y)
xz = dijkstra(x, z, y)

if xy != -1 and yz != -1:
    print(xy + yz, xz)
else:
    print(-1, xz)