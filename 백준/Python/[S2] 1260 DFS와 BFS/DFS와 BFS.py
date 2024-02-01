from collections import deque
import sys
input = sys.stdin.readline

# DFS
def dfs(x):
    # x와 연결된 정점 탐색
    for nx in connect[x]:
        if nx not in dfs_path:
            dfs_path.append(nx)
            dfs(nx)

##############################################################

# BFS
def bfs(x):
    # 탐색할 정점을 담은 큐
    q = deque([x])
    while q:
        p = q.popleft()
        for np in connect[p]:
            if np not in bfs_path:
                bfs_path.append(np)
                q.append(np)

##############################################################

global N

# 정점 수, 간선 수, 탐색 시작 정점
N, M, V = map(int, input().split())

# 연결 정보 (정점 번호가 작은 것부터 방문해야 하므로 정렬)
connect = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)
for c in connect:
    c.sort()

# DFS 결과
dfs_path = [V]
dfs(V)

# BFS 결과
bfs_path = [V]
bfs(V)

print(*dfs_path)
print(*bfs_path)