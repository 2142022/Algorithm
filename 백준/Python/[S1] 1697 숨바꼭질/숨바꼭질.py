from collections import deque
import sys
input = sys.stdin.readline

# BFS로 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 구하기
def bfs(N, K):
    # 수빈이가 이동하는 데 걸린 시간
    time = [0] * 100001

    # 수빈이의 위치를 담은 큐
    q = deque([N])
    while q:
        # 수빈이의 위치
        p = q.popleft()
        # 현재 위치까지 걸린 시간
        t = time[p]

        # -1, +1, X2
        for np in (p - 1, p + 1, 2 * p):
            # 동생의 위치인 경우 끝내기
            if np == K:
                return t + 1
            if 0 <= np <= 100000 and time[np] == 0:
                time[np] = t + 1
                q.append(np)

#############################################################3

# 수빈이 위치, 동생 위치
N, K = map(int, input().split())

# 둘의 위치가 같은 경우
if N == K:
    print(0)

# BFS로 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 구하기
else:
    print(bfs(N, K))