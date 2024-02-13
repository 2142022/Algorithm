from collections import deque

# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 노드 수, 간선 수
    N, E = map(int, input().split())

    # 연결 정보
    connect = [list() for _ in range(N)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        connect[u].append((v, w))

    # 0번 노드에서 각 노드까지 가는데 걸리는 최단 비용
    min_cost = [10 * E] * N
    min_cost[0] = 0

    # 탐색 노드와 현재까지의 가중치 합를 담은 큐
    q = deque([(0, 0)])
    while q:
        # 현재 노드, 현재까지의 가중치 합
        u, w = q.popleft()

        # 마지막 노드인 경우 끝내기
        if u == N - 1:
            min_cost[u] = min(min_cost[u], w)
            continue

        # 현재 경로가 최단 경로가 아닌 경우 패스
        if min_cost[u] != w:
            continue

        # 다음 노드 큐에 담기
        for v, nw in connect[u]:
            if min_cost[v] > w + nw:
                min_cost[v] = w + nw
                q.append((v, w + nw))

    print(f'#{T} {min_cost[N - 1]}')