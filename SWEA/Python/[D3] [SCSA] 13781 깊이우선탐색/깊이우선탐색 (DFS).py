# 노드 x와 연결된 노드 탐색
def dfs(x):
    for nx in connect[x]:
        if not visited[nx]:
            visited[nx] = 1
            path.append(str(nx))
            dfs(nx)

####################################################

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 노드 수, 간선 수
    V, E = map(int, input().split())

    # 연결 정보
    connect = [list() for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        connect[a].append(b)
        connect[b].append(a)

    # 낮은 정점부터 방문하기 위해 정렬
    for c in connect:
        c.sort()

    # 방문 체크
    visited = [0] * (V + 1)
    visited[1] = 1

    # 최종 탐색 경로
    path = ['1']

    # DFS로 노드 하나씩 방문
    dfs(1)

    print(f'#{t} {" ".join(path)}')