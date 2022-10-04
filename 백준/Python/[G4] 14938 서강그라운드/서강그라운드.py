import sys
input = sys.stdin.readline

def dijkstra(start):
    # 시작 노드는 거리가 0
    dist[start] = 0

    for i in range (n):
        min_d = 2147483647
        idx = 0

        # 선택하지 않은 정점 중 dist가 가장 짧은 것 고르기
        for j in range(1, n + 1):
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


# n: 지역의 개수, m: 수색 범위, r: 길의 개수
n, m, r = map(int, input().split())

# 각 구역 아이템 수
item = list(map(int, input().split()))

# r개의 간선 정보 저장
# 인접 리스트
edge = [[] for i in range(n + 1)]
for i in range(r):
    a, b, l = map(int, input().split())

    edge[a].append([b, l])
    edge[b].append([a, l])

# 예은이가 얻을 수 있는 최대 아이템 개수
max_item = 0

# 한 지역씩 시작 지점으로 두고 다른 지역까지의 거리 구하기
for i in range(n):
    # dist[i]: 시작 정점부터 i번째 정점까지의 최단 경로의 길이
    # 최대값으로 초기화
    dist = [2147483647] * (n + 1)

    # 방문 체크
    visit = [0] * (n + 1)
    
    dijkstra(i)

    # 예은이가 얻을 수 있는 아이템 개수
    cnt = 0

    # 수색 범위 내에 있는 지역의 아이템 개수 더하기
    for i in range(1, n + 1):
        if dist[i] <= m:
            cnt += item[i - 1]

    max_item = max(max_item, cnt)

# 결과 출력하기
print(max_item)
