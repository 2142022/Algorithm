from heapq import heappush, heappop
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 지도의 세로, 가로 길이
N, M = map(int, input().split())
# 지도
graph = [list(map(int, input().split())) for _ in range(N)]

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 섬 분류하기
alpha = ord('A')
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            # BFS로 현재 섬 모두 찾기
            q = deque([(i, j)])
            graph[i][j] = alpha
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 1:
                        graph[nr][nc] = alpha
                        q.append((nr, nc))
            alpha += 1

# 섬 개수
I = alpha - ord('A')

# 섬끼리 연결할 수 있는 최소 길이의 다리
bridge = defaultdict(lambda:100)
# 가로 다리
for i in range(N):
    j = 0
    while j < M - 1:
        if graph[i][j] >= ord('A') and graph[i][j + 1] == 0:
            start = graph[i][j]
            length = 1
            j += 2
            while j < M and graph[i][j] == 0:
                length += 1
                j += 1
            if j < M:
                end = graph[i][j]
                A, B = min(start, end), max(start, end)
                if length > 1:
                    bridge[(A, B)] = min(bridge[(A, B)], length)
                j -= 1
        j += 1
# 세로 다리
for j in range(M):
    i = 0
    while i < N - 1:
        if graph[i][j] >= ord('A') and graph[i + 1][j] == 0:
            start = graph[i][j]
            length = 1
            i += 2
            while i < N and graph[i][j] == 0:
                length += 1
                i += 1
            if i < N:
                end = graph[i][j]
                A, B = min(start, end), max(start, end)
                if length > 1:
                    bridge[(A, B)] = min(bridge[(A, B)], length)
                i -= 1
        i += 1

# 연결된 섬 중 가장 작은 숫자(알파벳)의 섬 찾기
def get_connect(x):
    if connect[x] != x:
        connect[x] = get_connect(connect[x])
    return connect[x]

# 섬 연결하기
result = 0
connect = [i for i in range(I)]
cnt = 0
h = []
for k, v in bridge.items():
    heappush(h, (v, k[0] - ord('A'), k[1] - ord('A')))
while h and cnt < I:
    c, a, b = heappop(h)
    A = get_connect(a)
    B = get_connect(b)
    if A != B:
        cnt += 1
        connect[max(A, B)] = connect[min(A, B)]
        result += c

# 모든 섬을 연결할 수 없는 경우 (다리 개수가 섬 개수 - 1이 아닌 경우)
if cnt != I - 1:
    print(-1)
else:
    print(result)