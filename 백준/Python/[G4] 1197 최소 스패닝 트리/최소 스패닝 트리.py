import heapq
import sys
input = sys.stdin.readline

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())

# 인접 리스트
edge = [[] for i in range(V + 1)]
for i in range(E):
    # 연결된 정점들과 간선의 가중치
    A, B, C = map(int, input().split())

    # 무향 그래프이므로 양 쪽에 다 넣어주기
    # 힙에 넣었을 때 가중치 기준으로 오름차순 정렬하기 위해 가중치 먼저 넣기
    edge[A].append((C, B))
    edge[B].append((C, A))

# 방문체크
visit = [0] * (V + 1)

# 방문한 정점의 개수
cnt = 0

# 결과: 최소 가중치
result = 0

# 최소 힙
q = []

# 정점 1부터 시작 (아무 정점부터 시작해도 됨)
# 힙에 정점 1에 연결된 정점 모두 넣기
for i in edge[1]:
    heapq.heappush(q, i)
visit[1] = 1
cnt += 1

# 모든 정점을 선택하면 끝내기
while cnt != V:
    # 가중치가 가장 작은 간선 뽑기
    now = heapq.heappop(q)

    # 이미 방문한 정점이라면 pass
    if visit[now[1]] == 1:
        continue

    result += now[0]
    visit[now[1]] = 1
    cnt += 1

    # 현재 정점에 연결된 정점 모두 힙에 넣기
    for i in edge[now[1]]:
        heapq.heappush(q, i)

print(result)
