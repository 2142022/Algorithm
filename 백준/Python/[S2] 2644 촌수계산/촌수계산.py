from collections import deque
import sys
input = sys.stdin.readline

# 두 사람 s, e의 촌수 구하기
def bfs(s, e):
    # s와의 촌수
    dist = [-1] * (n + 1)
    dist[s] = 0

    # 탐색하는 사람을 담은 큐
    q = deque([s])
    while q:
        # 현재 사람
        p = q.popleft()

        # 현재 사람까지의 거리
        d = dist[p]

        # 현재 사람과 연결된 사람 탐색
        for np in connect[p]:
            # 아직 탐색하지 않은 경우 탐색
            if dist[np] == -1:
                # 원하는 사람까지 도착한 경우
                if np == e:
                    return d + 1

                dist[np] = d + 1
                q.append(np)

    # 친척 관계가 전혀 없는 경우
    return -1

#######################################################3

global n

# 전체 사람 수
n = int(input())

# 촌수를 계산해야 하는 서로 다른 두 사람
s, e = map(int, input().split())

# 관계 수
m = int(input())

# 관계
connect = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

# 두 사람 간의 촌수 구하기
print(bfs(s, e))