import heapq
import sys
input = sys.stdin.readline

# 논의 수
N = int(input())

# 논에 우물을 팔 때 드는 비용
W = [0] * N
for i in range(N):
    W[i] = int(input())

# 논을 연결하는데 드는 비용
P = [0] * N
for i in range(N):
    P[i] = list(map(int, input().split()))

# 방문 체크
visit = [0] * N

# 방문한 논의 개수
cnt = 0

# 최소 비용
result = 0

# 최소 힙
q = []

# 원래 시작 지점을 정해서 힙에 넣지만,
# 어차피 적어도 하나의 논은 우물을 파야 하므로
# 모든 논의 우물 팔 때 비용을 힙에 넣기
# 비용을 기준으로 오름차순 정렬해야 하므로 비용을 먼저 넣기
for i in range(N):
    heapq.heappush(q, (W[i], i))

# 모든 논을 방문할 때까지 반복
while cnt != N:
    # 가장 적은 비용을 뽑기
    now = heapq.heappop(q)

    # 이미 방문한 논은 pass
    if visit[now[1]] == 1:
        continue

    visit[now[1]] = 1
    cnt += 1
    result += now[0]

    # 현재 논과 연결된 다른 논과의 연결 비용을 힙에 넣기
    for i in range(N):
        if i != now[1]:
            heapq.heappush(q, (P[now[1]][i], i))

print(result)
