from collections import deque
import sys
input = sys.stdin.readline

# 수빈이 위치, 동생 위치
N, K = map(int, input().split())

# 수빈이와 동생의 위치가 같은 경우
if N == K:
    print(0)
    exit()

# 수빈이가 각 지점까지 가는데 걸리는 시간
time = [-1] * 100001
time[N] = 0

# 수빈이의 위치를 담은 큐
q = deque([N])
while q:
    # 수빈이의 위치
    p = q.popleft()

    # 현재 위치까지 이동하는데 걸리 시간
    t = time[p]

    # 다른 곳으로 이동하기
    for np in (p - 1, p + 1, 2 * p):
        if 0 <= np <= 100000 and time[np] == -1:
            if np == K:
                print(t + 1)
                exit()
            time[np] = t + 1
            q.append(np)
