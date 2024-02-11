from collections import deque
import sys
input = sys.stdin.readline

# 노드 개수, 간선 개수
N, M = map(int, input().split())

# 연결 정보
connect = [list() for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

# 방문 체크
visited = [0] * (N + 1)

# 연결 요소 개수
cnt = 0

# 연결 요소 찾기
for i in range(1, N + 1):
    # 이미 연결 요소에 포함된 경우 패스
    if visited[i]:
        continue
    visited[i] = 1
    cnt += 1

    # 탐색할 노드를 담은 큐
    q = deque([i])
    while q:
        n = q.popleft()

        # 연결된 노드 탐색
        for nn in connect[n]:
            if not visited[nn]:
                visited[nn] = 1
                q.append(nn)

print(cnt)