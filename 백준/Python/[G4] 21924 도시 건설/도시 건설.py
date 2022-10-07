import heapq
import sys
input = sys.stdin.readline

# N: 건물의 개수, M: 도로의 개수
N, M = map(int, input().split())

# 총 도로 건설 비용
total = 0

# 인접리스트
road = [[] for i in range(N+1)]
for i in range(M):
    # 건물의 번호와 도로 건설 비용
    a, b, c = map(int, input().split())
    total += c

    # 무향 그래프이므로 양쪽 건물에 추가
    # 비용 기준으로 오름차순 정렬하기 위해 비용 먼저 넣기
    road[a].append((c, b))
    road[b].append((c, a))

# 건물 방문 체크
visit = [0] * (N+1)

# 방문한 건물 개수
cnt = 0

# 최소 도로 건설 비용
result = 0

# 최소 힙
q = []

# 도로1부터 시작(아무 도로에서부터 시작해도 됨)
# 도로1에 연결된 도로를 힙에 넣기
for i in road[1]:
    heapq.heappush(q, i)
cnt += 1
visit[1] = 1

# q가 비거나 모든 건물을 방문하면 그만두기
while q and cnt != N:
    # 도로 하나 뽑기
    now = heapq.heappop(q)

    # 이미 방문한 건물이면 pass
    if visit[now[1]] == 1:
        continue
    
    result += now[0]
    cnt += 1
    visit[now[1]] = 1

    # 현재 건물과 연결된 건물 모두 힙에 넣기
    for i in road[now[1]]:
        heapq.heappush(q, i)

# 모든 건물을 방문하지 못했으면 모든 건물이 연결되지 않았으므로 -1 출력
if cnt != N:
    print(-1)
else:
    # 절약 비용 출력
    print(total - result)
