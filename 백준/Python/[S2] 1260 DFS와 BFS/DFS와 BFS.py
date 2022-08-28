import sys
input = sys.stdin.readline

# DFS
def dfs(num):
    # 방문 체크하고 출력
    visit[num] = 1
    print(num, end = ' ')

    # 아직 방문하지 않았고 현재 노드와 연결되어 있는 노드들 재귀
    for i in range(N+1):
        if visit[i] == 0 and edge[num][i] == 1:
            dfs(i)

# BFS
def bfs(num):
    # 방문 체크하고 tmp에 추가
    visit[num] = 1
    tmp = []
    tmp.append(num)

    # tmp에 원소가 없을 때까지 반복
    while len(tmp) != 0:
        # 첫 번째 원소 pop하고 출력
        n = tmp.pop(0)
        print(n, end = ' ')

        # 아직 방문하지 않았고 현재 노드(n)와 연결되어 있는 노드들 tmp에 추가
        for i in range(N+1):
            if visit[i] == 0 and edge[n][i] == 1:
                tmp.append(i)
                visit[i] = 1

# 노드 개수, 간선 개수, 루트 노드 번호
N, M, V = map(int, input().split())

# 노드가 연결되어 있으면 1, 아니면 0
edge = [[0] * (N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    edge[a][b] = edge[b][a] = 1

# 방문한 노드는 1, 아니면 0
visit = [0] * (N+1)

dfs(V)
print()

# visit 초기화
visit = [0] * (N+1)
bfs(V)
