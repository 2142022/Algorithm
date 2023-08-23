from collections import deque
import sys
input = sys.stdin.readline

# 정점 x와 거리가 가장 먼 정점과 그 거리 반환
def find_max_distance(x):
    global V

    # 가장 먼 거리
    max_distance = 0
    # 가장 먼 거리에 있는 정점
    max_node = 0

    # 방문 체크용
    visited = [0] * (V + 1)

    # 현재 정점과 현재까지의 거리를 담은 큐
    q = deque()
    q.append((x, 0))

    # 큐가 빌 때까지 반복
    while q:
        # 현재 정점과 현재까지의 거리
        node, distance = q.popleft()

        # 정점 x로부터 가장 먼 거리에 있는 정점이라면 갱신
        if distance > max_distance:
            max_node = node
            max_distance = distance

        # 방문체크
        visited[node] = 1

        # 연결된 정점 큐에 담기
        for n, d in connect[node]:
            # 이미 방문한 곳은 패스
            if visited[n]:
                continue

            # 큐에 추가
            q.append((n, distance + d))

    return max_node, max_distance

####################################################################

# 정점의 개수
V = int(input())

# 각 정점에 연결된 간선 정보
# ex) connect[3] = [(1, 2), (4, 3)]
#     : 정점3은 정점1과의 거리가 2, 정점4와의 거리가 3로 연결되어 있음
connect = [[] for _ in range(V + 1)]
for _ in range(V):
    # 간선정보
    edge = list(map(int, input().split()))

    # 현재 정점 번호
    n = edge[0]

    # 정점 n과 연결된 간선 정보 추가
    for i in range(1, len(edge) - 1, 2):
        connect[n].append((edge[i], edge[i + 1]))

# 정점1과 거리가 가장 먼 정점과 그 거리
n, d = find_max_distance(1)

# 정점 n과 가장 먼 거리 출력
print(find_max_distance(n)[1])