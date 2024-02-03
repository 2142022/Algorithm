from collections import deque
import sys
input = sys.stdin.readline

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간과 그 경우의 수 구하기
def bfs(N, K):
    # 수빈이가 동생을 찾을 수 있는 가장 빠른 시간과 그 경우의 수
    time, cnt = 100000, 0

    # 방문 체크 (그 위치에 도착하는 시간)
    visited = [-1] * 100001
    visited[N] = 0

    # 수빈이 위치를 담은 큐
    q = deque([N])
    while q:
        # 수빈이 위치
        p = q.popleft()
        # 걸린 시간
        t = visited[p]

        # 수빈이가 동생을 찾은 시간 이상인 경우 끝내기
        if t >= time:
            break

        # 수빈이의 다음 위치
        for np in (p + 1, p - 1, 2 * p):
            # 목적지인 경우
            if np == K:
                time = t + 1
                cnt += 1
                continue

            # 다음 위치 큐에 넣기
            if 0 <= np <= 100000 and visited[np] in (-1, t + 1):
                visited[np] = t + 1
                q.append(np)

    return time, cnt

######################################################################

# 수빈이 위치, 동생 위치
N, K = map(int, input().split())

# 수빈이와 동생이 같은 위치에 있는 경우
if N == K:
    print(0)
    print(1)
else:
    print(*bfs(N, K), sep='\n')