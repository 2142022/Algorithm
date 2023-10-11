from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 정점 X로부터 각 정점까지의 거리 반환
def dijkstra(x):
    # 정점 X로부터 각 정점까지의 거리
    dist = [sys.maxsize] * (N + 1)
    dist[x] = 0

    # 현재까지의 거리, 현재 정점을 담은 최소 힙
    h = []
    heappush(h, (0, x))

    # 힙 탐색
    while h:
        # 현재까지의 거리, 현재 정점
        d, u = heappop(h)

        # 기존 거리보다 크다면 패스
        if d > dist[u]:
            continue

        # 연결 정점 탐색
        for w, v in connect[u]:
            # 기존 거리보다 짧은 경우 힙에 추가
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(h, (d + w, v))

    return dist

###################################################

# 정점 수, 간선 수
N, M = map(int, input().split())

# 연결 정보
connect = [list() for _ in range(N + 1)]
for _ in range(M):
    # 도시 u와 도시 v 사이의 가중치 w
    u, v, w = map(int, input().split())
    connect[u].append((w, v))
    connect[v].append((w, u))

# 출발 정점, 도착 정점
X, Z = map(int, input().split())

# 중간 정점 개수
P = int(input())
# 중간 정점
Y = list(map(int, input().split()))

# X로부터의 거리
distX = dijkstra(X)
# Z로부터의 거리
distY = dijkstra(Z)

# 도시 X와 도시 Z 사이의 최단 경로 거리
d = sys.maxsize

# 중간 정점 탐색
for i in Y:
    # 도시 X와 도시 Z 사이의 최단 경로 거리
    # = (도시 X부터 도시 i까지의 최단 경로 거리) + (도시 i부터 도시 Z까지의 최단 경로 거리)
    d = min(d, distX[i] + distY[i])

# 경로가 없는 경우 -1 출력
if d == sys.maxsize:
    print(-1)
else:
    print(d)