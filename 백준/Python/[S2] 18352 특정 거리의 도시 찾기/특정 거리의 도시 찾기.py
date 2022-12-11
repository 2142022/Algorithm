from collections import deque
import sys
input = sys.stdin.readline

# BFS를 이용하여 X번 도시부터 각 도시까지의 최단 거리 구하기
def get_dist(X):
    # N(도시의 개수): 전역 변수
    global N

    # 현재 도시 번호가 담긴 큐
    q = deque()
    # 큐에 출발 도시 번호 넣기
    q.append(X)

    # 큐에 원소가 없어질 때까지 반복
    while q:
        # 현재 도시 번호
        now = q.popleft()

        # 현재까지의 거리가 K보다 크다면 끝내기
        if dist[now] > K:
            break

        # 현재 도시와 연결된 도시 탐색
        for i in connect[now]:
            # 출발 도시는 패스
            if i == X:
                continue

            # 아직 방문하지 않았다면 거리 갱신 후, 큐에 현재 도시 번호 넣기
            if dist[i] == 0:
                dist[i] = dist[now] + 1
                q.append(i)

######################################################################

# N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시 번호
N, M, K, X = map(int, input().split())

# 인접 리스트: connect[i]는 i번 도시에서 갈 수 있는 모든 도시 번호
connect = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    connect[i].append(j)

# X번 도시부터 각 도시까지의 최단 거리
dist = [0] * (N + 1)

# BFS를 이용하여 X번 도시부터 각 도시까지의 최단 거리 구하기
get_dist(X)

# 최단 거리가 K인 도시의 개수
cnt = 0

# 최단 거리가 K인 도시 번호 출력
for i in range(1, N + 1):
    if dist[i] == K:
        cnt += 1
        print(i)

# 최단 거리가 K인 도시가 없는 경우 -1 출력
if cnt == 0:
    print(-1)
