from collections import deque
import sys
input = sys.stdin.readline

# 노드 개수, 시작 노드, 목표 노드
N, S, E = map(int, input().split())

# 연결 정보
connect = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

# 각 노드의 부모 노드
parent = [-1] * (N + 1)
parent[E] = 0

# 탐색 노드를 담은 큐
q = deque([E])
while q:
    node = q.popleft()
    for nn in connect[node]:
        if parent[nn] == -1:
            parent[nn] = node
            q.append(nn)

# 현재 노드
now = S

# 선공 여부
first = 1

# 게임 진행
while now != E:
    # 후공이 갈 수 있는 정점이 3개 이상이라면 무조건 후공 승리
    # 1개는 시작 노드로 가는 길, 다른 1개는 목표 노드로 가는 길
    if not first and len(connect[now]) > 2:
        print('Second')
        break

    # 턴 바꾸기
    first ^= 1
    now = parent[now]

# 선공 승리
else:
    print('First')