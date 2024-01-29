from collections import deque
import sys
input = sys.stdin.readline

# 사람 수
n = int(input())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, input().split())

# 관계 수
m = int(input())

# 각 사람마다 연결된 사람의 번호
connect = [list() for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    connect[x].append(y)
    connect[y].append(x)

# 방문 체크
visited = 1 << a

# 탐색하는 사람과 a와의 촌수를 담은 큐
q = deque([(a, 0)])
while q:
    # 현재 사람, 현재 사람과 a와의 촌수
    p, cnt = q.popleft()

    # b인 경우 끝내기
    if p == b:
        print(cnt)
        break

    # 연결된 사람 체크
    for np in connect[p]:
        if not visited & 1 << np:
            visited |= 1 << np
            q.append((np, cnt + 1))

# a, b 사이에 아무 관계가 없는 경우
else:
    print(-1)