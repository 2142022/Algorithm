from collections import deque
import sys
input = sys.stdin.readline

# 도시 개수
N = int(input())
# 버스 개수
M = int(input())

# 버스 정보
bus = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    bus[A].append((B, C))

# 출발점과 도착점
s, d = map(int, input().split())

# 출발점에서 다른 도시로 가는데 드는 최소 비용
cost = [sys.maxsize] * (N + 1)
cost[s] = 0

# 도시 번호와 비용을 담은 큐
q = deque([(s, 0)])

# 버스 탐색
while q:
    # 도시 번호와 현재까지의 비용
    a, c = q.popleft()

    # 기존 비용보다 크다면 패스
    if c > cost[a]:
        continue

    # 다음 방문할 곳 큐에 넣기
    for na, nc in bus[a]:
        # 최소 비용 갱신
        if nc + c < cost[na]:
            cost[na] = nc + c
            q.append((na, nc + c))

print(cost[d])
