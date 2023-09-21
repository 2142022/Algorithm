from collections import deque
import sys, heapq
input = sys.stdin.readline

# MST 비용 구하기
def get_mst():
    global N, M, cost

    # 방문 체크
    visited = [0] * (N + 1)
    # 방문한 정점 개수
    cnt = 0

    # mst비용
    mst = 0

    # 탐색할 간선 정보를 담은 최소 힙
    h = []
    heapq.heappush(h, (0, 1))

    # 간선 탐색
    while h:
        # 현재까지의 비용과 현재 정점 번호
        c, a = heapq.heappop(h)

        # 방문체크
        if visited[a]:
            continue
        visited[a] = 1
        cnt += 1
        mst += c

        # 모든 정점 탐색한 경우 끝내기
        if cnt == N:
            cost = mst
            return

        # 다음 정점 탐색
        for nc, na in edge[a]:
            if not visited[na]:
                heapq.heappush(h, (nc, na))

    # MST를 만들지 못한 경우 0 반환
    cost = 0

##################################################

# N: 정점 개수, M: 간선 개수, K: 턴 수
N, M, K = map(int, input().split())

# 간선 정보
edge = [deque() for _ in range(N + 1)]
# 각 턴마다 삭제할 간선에 연결된 정점 번호
remove = dict()
for i in range(1, M + 1):
    a, b = map(int, input().split())
    edge[a].append((i, b))
    edge[b].append((i, a))
    remove[i] = (a, b)

# MST 비용
cost = 1

# K번 반복
for k in range(1, K + 1):
    # MST를 만들 수 없다면 바로 0 출력
    if cost == 0:
        print(0, end = ' ')
        continue

    # MST비용 구하기
    get_mst()
    print(cost, end = ' ')

    # MST를 만들 수 있는 경우, 간선 하나 삭제
    # 양방향 간선이므로 2번 삭제
    if cost:
        # 삭제할 간선에 연결된 정점 번호
        a, b = remove[k]
        edge[a].popleft()
        edge[b].popleft()
        M -= 1