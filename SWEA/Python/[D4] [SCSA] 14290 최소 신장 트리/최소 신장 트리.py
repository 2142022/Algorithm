from heapq import heappush, heappop

# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 노드 개수, 간선 개수
    V, E = map(int, input().split())

    # 연결 정보
    connect = [list() for _ in range(V + 1)]
    for _ in range(E):
        # 두 노드, 가중치
        n1, n2, w = map(int, input().split())
        connect[n1].append((n2, w))
        connect[n2].append((n1, w))

    # 방문 체크
    visited = [0] * (V + 1)

    # 최소 신장 트리의 가중치 합
    s = 0

    # 가중치, 노드가 담긴 최소 힙
    h = []
    heappush(h, (0, 0))
    while h:
        # 가장 작은 가중치, 노드
        w, n = heappop(h)

        # 최소 신장 트리에 넣기
        if not visited[n]:
            visited[n] = 1
            s += w

            # 연결된 노드 탐색
            for ni, nw in connect[n]:
                # 아직 최소 신장 트리에 포함되지 않은 경우 힙에 넣기
                if not visited[ni]:
                    heappush(h, (nw, ni))

    print(f'#{T} {s}')
