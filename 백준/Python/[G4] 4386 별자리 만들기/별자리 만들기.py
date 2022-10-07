import heapq
import sys
input = sys.stdin.readline

# 별의 개수
n = int(input())

# 별들의 좌표
pos = [0] * n
for i in range(n):
    pos[i] = list(map(float, input().split()))

# 별들 사이의 거리(=비용)
dist = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(i+1, n):
        dist[i][j] = (((pos[i][0] - pos[j][0]) ** 2) + ((pos[i][1] - pos[j][1]) ** 2)) ** 0.5
        dist[j][i] = dist[i][j]

# 방문 체크
visit = [0] * n

# 방문한 별의 개수
cnt = 0

# 별자리를 만들 수 있는 최소 비용
result = 0

# 최소 힙
q = []

# 0번 별부터 시작 (아무데서나 시작해도 됨)
# 0번 별을 제외한 다른 별들을 힙에 넣기
# 비용 기준으로 오름차순 정렬하기 위해 비용 먼저 힙에 넣기
for i in range(1, n):
    heapq.heappush(q, (dist[0][i], i))
visit[0] = 1
cnt += 1

# 모든 별을 방문할 때까지 반복
while cnt != n:
    # 가장 짧은 거리 뽑기
    now = heapq.heappop(q)

    # 이미 방문한 별이면 pass
    if visit[now[1]] == 1:
        continue

    result += now[0]
    cnt += 1
    visit[now[1]] = 1

    # 현재 별을 제외한 다른 별들을 힙에 넣기
    for i in range(0, n):
        if i != now[1]:
            heapq.heappush(q, (dist[now[1]][i], i))

print(format(result, ".2f"))
