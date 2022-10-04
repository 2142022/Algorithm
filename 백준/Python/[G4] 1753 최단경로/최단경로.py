import sys
input = sys.stdin.readline

def dijkstra(start):
    # 시작 노드는 거리가 0
    dist[start] = 0

    for i in range (V):
        min_d = 2147483647
        idx = 0

        # 선택하지 않은 정점 중 dist가 가장 짧은 것 고르기
        for j in range(1, V + 1):
            if visit[j] == 0 and dist[j] < min_d:
                min_d = dist[j]
                idx = j

        # 방문 체크
        visit[idx] = 1

        # 뽑은 친구와 연결되어 있는 간선들 갱신하기
        for i in edge[idx]:
            # 방문하지 않았고, 갱신할 수 있을 때
            # 갱신: 이미 가지고 있는 값보다 (idx까지 온 길이 + 앞으로 갈 길이)가 더 작은 경우
            if visit[i[0]] == 0 and dist[i[0]] > dist[idx] + i[1]:
                dist[i[0]] = dist[idx] + i[1]



    

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())

# 시작 정점의 번호
K = int(input())

# E개의 간선 정보 저장
# 인접 리스트
edge = [[] for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())

    edge[u].append([v, w])


# dist[i]: 시작 정점부터 i번째 정점까지의 최단 경로의 길이
# 최대값으로 초기화
dist = [2147483647] * (V + 1)

# 방문 체크
visit = [0] * (V + 1)

dijkstra(K)

# 결과 출력하기
for i in range(1, V + 1):
    if visit[i] == 1:
        print(dist[i])
    else:
        print("INF")

