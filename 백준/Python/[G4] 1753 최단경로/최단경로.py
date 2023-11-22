from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())

# 시작 정점의 번호
K = int(input())

# 연결 정보
connect = [defaultdict(int) for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    if v not in connect[u]:
        connect[u][v] = w
    elif w < connect[u][v]:
        connect[u][v] = w

# dist[i]: 시작 정점부터 i번째 정점까지의 최단 경로의 길이
dist = [sys.maxsize] * (V + 1)
dist[0] = dist[K] = 0

# 탐색할 노드
h = []
heapq.heappush(h, ((0, K)))
while h:
    # 현재까지의 거리 및 노드
    d, n = heapq.heappop(h)

    # 최단 거리가 아닌 경우 패스
    if dist[n] < d:
        continue

    # 현재 노드와 연결된 노드 탐색
    for v, w in connect[n].items():
        # 기존 거리보다 작은 경우 큐에 추가
        if d + w < dist[v]:
            heapq.heappush(h, (d + w, v))
            dist[v] = d + w

# 결과 출력하기
for i in range(1, V + 1):
    if dist[i] != sys.maxsize:
        print(dist[i])
    else:
        print("INF")