# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 노드 수, 간선 수
    V, E = map(int, input().split())

    # 각 노드별 연결된 노드
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

    # 탐색 경로를 담은 스택
    stack = [1]

    # 모든 탐색 경로
    path = ['1']

    while stack:
        # 마지막 방문 노드
        last = stack[-1]

        # 아직 방문하지 않은 노드 탐색
        for next in connect[last]:
            if not visited[next]:
                stack.append(next)
                path.append(str(next))
                visited[next] = 1
                break

        # 현재 노드에서 더 이상 탐색할 수 있는 노드가 없는 경우, 스택에서 현재 노드 꺼내기
        else:
            stack.pop()

    print(f'#{t} {" ".join(path)}')
