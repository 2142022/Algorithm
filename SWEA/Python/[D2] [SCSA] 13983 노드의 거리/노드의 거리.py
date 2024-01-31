from collections import deque

# S와 G의 거리 구하기
def bfs(S, G):
    # 출발 노드와의 거리
    dist = [0] * (V + 1)

    # 현재 노드를 담은 큐
    q = deque([S])
    while q:
        # 현재 노드
        n = q.popleft()

        # 현재까지의 이동 거리
        d = dist[n]

        # 연결된 노드 탐색
        for nn in connect[n]:
            # 아직 방문하지 않은 경우
            if not dist[nn]:
                # 거리 갱신
                dist[nn] = d + 1

                # 도착 노드인 경우 끝내기
                if nn == G:
                    return dist[nn]

                # 큐에 다음 노드 넣기
                q.append(nn)

    # 출발 노드와 도착 노드가 연결되어 있지 않은 경우
    return 0

###########################################################

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

    # 출발 노드, 도착 노드
    S, G = map(int, input().split())

    print(f'#{t} {bfs(S, G)}')



