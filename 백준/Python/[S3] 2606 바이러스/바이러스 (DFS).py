import sys
input = sys.stdin.readline

# x번 컴퓨터와 연결된 컴퓨터 탐색
def dfs(x):
    for nx in connect[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx)

###################################################

# 컴퓨터 수
N = int(input())

# 연결 수
M = int(input())

# 연결 정보
connect = [list() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

# 방문 체크
visited = [0] * (N + 1)
visited[1] = 1

# DFS로 연결된 컴퓨터 탐색
dfs(1)

# 1번 컴퓨터를 제외하고 바이러스에 걸리는 컴퓨터 수 출력
print(sum(visited) - 1)