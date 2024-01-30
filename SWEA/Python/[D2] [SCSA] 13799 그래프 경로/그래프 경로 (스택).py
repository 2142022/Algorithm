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

    # 출발 노드, 도착 노드
    S, G = map(int, input().split())

    # 방문 체크
    visited = [0] * (V + 1)
    visited[S] = 1

    # 방문한 경로를 담은 스택
    stack = [S]
    while stack:
        # 현재 노드
        n = stack[-1]

        # 목적지인 경우 끝내기
        if n == G:
            print(f'#{t} 1')
            break

        # 현재 노드와 연결된 노드 탐색
        for nn in connect[n]:
            if not visited[nn]:
                visited[nn] = 1
                stack.append(nn)
                break

        # 현재 노드에서 더 이상 탐색할 수 있는 경로가 없는 경우
        else:
            stack.pop()

    # S와 G가 연결되지 않은 경우
    else:
        print(f'#{t} 0')