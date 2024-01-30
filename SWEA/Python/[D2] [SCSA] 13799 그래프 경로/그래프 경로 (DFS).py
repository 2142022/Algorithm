# 노드 x에서 갈 수 있는 노드 탐색
def dfs(x):
    global G

    # 이미 도착지까지 도착한 경우 끝내기
    if visited[G]:
        return

    # 현재 노드와 연결된 노드 탐색
    for nx in connect[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx)

#####################################################

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

    # 출발 노드, 도착 노드
    S, G = map(int, input().split())

    # 방문 체크
    visited = [0] * (V + 1)
    visited[S] = 1

    # DFS로 노드 하나씩 방문
    dfs(S)

    print(f'#{t} {visited[G]}')