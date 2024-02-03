from collections import deque
import sys
input = sys.stdin.readline

# G층에 가기 위해 눌러야 하는 버튼 수 구하기
def bfs(F, S, G, U, D):
    # 각 층별까지 이동하는데 눌러야 하는 최소 버튼 수
    cnt = [-1] * (F + 1)
    cnt[S] = 0

    # 현재 위치를 담은 큐
    q = deque([S])
    while q:
        # 현재 위치
        p = q.popleft()

        # 현재 위치까지 누른 버튼 수
        c = cnt[p]

        # 다음 위치
        for np in (p + U, p - D):
            # 목적지인 경우
            if np == G:
                return c + 1

            # 범위 및 방문 체크
            if 0 < np <= F and cnt[np] == -1:
                cnt[np] = c + 1
                q.append(np)

    # 목적지까지 이동할 수 없는 경우
    return 'use the stairs'

#########################################################################

# 건물 층수, 강호 위치, 목적지, 위로 갈 수 있는 층, 아래로 갈 수 있는 층
F, S, G, U, D = map(int, input().split())

# 출발지와 목적지가 같은 경우
if S == G:
    print(0)

# G층에 가기 위해 눌러야 하는 버튼 수
else:
    print(bfs(F, S, G, U, D))