import heapq
import sys
input = sys.stdin.readline

# N: 황선자와 우주신들의 총 인원(?), M: 이미 연결된 통로의 개수
N, M = map(int, input().split())

# 황선자와 우주신들의 좌표
pos = [0] * (N+1)
for i in range(1, N+1):
    pos[i] = list(map(int, input().split()))

# 인접행렬 (통로의 길이)
path = [[0] * (N+1) for i in range(N+1)]
for i in range(1, N+1):
    for j in range(i+1, N+1):
        path[i][j] = (((pos[i][0] - pos[j][0]) ** 2) + ((pos[i][1] - pos[j][1]) ** 2)) ** 0.5
        path[j][i] = path[i][j]

# 이미 연결된 통로는 길이를 0으로 만들기
for i in range(M):
    a, b = map(int, input().split())
    path[a][b] = 0
    path[b][a] = 0

# 방문 체크
visit = [0] * (N+1)

# 방문한 인원
cnt = 0

# 최소 통로 길이
result = 0

# 최소 힙
q = []

# 1번부터 시작 (아무데서나 시작해도 됨)
# 모두가 서로 연결되어 있으므로 1번을 제외한 모든 우주신(혹은 황선자)을 힙에 넣기
for i in range(2, N+1):
    # 통로 길이 기준으로 오름차순 정렬하기 위해 통로 길이 먼저 넣기)
    heapq.heappush(q, (path[i][1], i))
visit[1] = 1
cnt += 1

# 모든 우주신(혹은 황선자)을 방문하면 끝내기
while cnt != N:
    # 길이가 가장 짧은 통로 뽑기
    now = heapq.heappop(q)

    # 이미 방문했으면 pass
    if visit[now[1]] == 1:
        continue

    result += now[0]
    visit[now[1]] = 1
    cnt += 1

    # 현재 우주신(혹은 황선자)을 제외한 모든 우주신(혹은 황선자)을 힙에 넣기
    for i in range(1, N+1):
        if i == now[1]:
            continue

        heapq.heappush(q, (path[now[1]][i], i))

# 소수점 둘째 자리까지 출력
print(format(result, ".2f"))
