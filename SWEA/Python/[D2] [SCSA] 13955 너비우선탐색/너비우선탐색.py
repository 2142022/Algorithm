from collections import deque

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 노드 수, 간선 수
    V, E = map(int, input().split())

    # 간선 정보
    connect = [list() for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        connect[a].append(b)
        connect[b].append(a)

    # 탐색 경로
    path = []

    # 방문 체크
    visited = [0] * (V + 1)
    visited[1] = 1

    # 현재 위치를 담은 큐
    q = deque([1])
    while q:
        # 현재 위치
        p = q.popleft()
        path.append(str(p))

        # 연결된 노드 탐색
        # 낮은 정점부터 방문해야 하므로 정렬
        for np in sorted(connect[p]):
            if not visited[np]:
                visited[np] = 1
                q.append(np)

    print(f'#{t} {" ".join(path)}')