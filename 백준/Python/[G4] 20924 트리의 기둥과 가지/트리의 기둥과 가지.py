from collections import deque
import sys
input = sys.stdin.readline

# 기둥 길이 구하기
def get_len():
    global R, RL

    while len(connect[R]) <= 2:
        for r, l in connect[R]:
            if not visited[r]:
                R = r
                RL += l
                visited[R] = 1

        # 가지가 없는 경우 끝내기
        if len(connect[R]) == 1:
            break

#################################################

# 노드 개수, 루트 노드
N, R = map(int, input().split())

# 연결 정보
connect = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, d = map(int, input().split())
    connect[a].append((b, d))
    connect[b].append((a, d))

# 방문 체크
visited = [0] * (N + 1)
visited[R] = 1

# 기둥의 길이
RL = 0

# 기둥이 있는 경우
if len(connect[R]) == 1:
    get_len()

# 가장 긴 가지 길이
LL = 0

# 탐색 노드와 가지 길이를 담은 큐
q = deque([(R, 0)])
while q:
    # 현재 노드, 현재까지의 가지 길이
    n, l = q.popleft()
    LL = max(LL, l)

    # 연결 노드 탐색
    for nn, nl in connect[n]:
        if not visited[nn]:
            visited[nn] = 1
            q.append((nn, l + nl))

# 기둥의 길이, 가장 긴 가지의 길이
print(RL, LL)