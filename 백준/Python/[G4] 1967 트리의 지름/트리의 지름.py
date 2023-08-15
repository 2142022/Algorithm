from collections import deque
import sys
input = sys.stdin.readline

# 노드 x로부터 가장 거리가 먼 노드까지의 거리 반환
def get_distance(x):
    global n

    # 가장 먼 거리
    max_dist = 0
    # 가장 먼 거리의 노드 번호
    max_node = 0

    # 방문 체크용
    visited = [0] * (n + 1)

    # 노드와 루트 노드부터의 가중치 정보를 담은 큐
    q = deque()
    q.append((x, 0))

    # 큐가 빌 때까지 반복
    while q:
        # node: 현재 노드, weight: 노드 x부터 현재까지의 거리
        node, dist = q.popleft()

        # 거리가 최대 거리보다 크다면 갱신
        if dist > max_dist:
            max_dist = dist
            max_node = node

        # 방문체크
        visited[node] = 1

        # 연결된 노드와 그 노드까지의 거리를 큐에 넣기
        for i, j in edges[node]:
            # 방문한 노드면 패스
            if visited[i]:
                continue

            # 큐에 넣기
            q.append((i, j + dist))

    return max_node, max_dist

#####################################################################

# 노드의 개수
n = int(input())

# 연결된 노드와 가중치 정보
edges = [[] for _ in range(n + 1)]

# 간선 정보 입력받기
for _ in range(n - 1):
    # a: 부모 노드, b: 자식 노드, c: 가중치
    a, b, c = map(int, input().split())

    edges[a].append((b, c))
    edges[b].append((a, c))

# 루트 노드로부터 가장 거리가 먼 노드 A를 구한 후,
# 노드 A로부터 가장 거리가 먼 노드까지의 거리 출력하기
print(get_distance(get_distance(1)[0])[1])