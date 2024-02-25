from collections import deque
import sys
input = sys.stdin.readline

# 원을 트리 구조로 나타내기
# i: 현재 원
# prev: 현재 원의 바깥쪽 원
def tree(i, prev):
    global max_level, max_circle

    # 현재 추가하려는 원이 i원의 내부 원들 중 그 내부에 있는 경우
    for j in connect[i]:
        # 바깥원 패스
        if j == prev:
            continue

        # 내부에 있는 경우
        x1, y1, R1 = circles[j]
        if (x - x1) ** 2 + (y - y1) ** 2 <= (R - R1) ** 2:
            tree(j, i)
            break

    # 현재 원의 내부에 추가하기
    else:
        connect[i].append(idx)
        connect[idx].append(i)
        level[idx] = level[i] + 1
        if level[idx] >= max_level:
            max_level = level[idx]
            max_circle = idx

#########################################################################################################################

# 가장 레벨이 높은 리프 노드에서 다른 노드까지의 최대 거리
def get_dist(i):
    # 다른 원까지의 거리
    dist = [0] * (N + 1)

    # 방문 체크
    visited = [0] * (N + 1)
    visited[i] = 1

    # 모든 원이 한 원의 내부에 있는 경우, 최상위 노드는 가장 바깥쪽 원이 되어야 함
    if len(connect) == 1:
        visited[0] = 1

    # 탐색 원을 담은 큐
    q = deque([i])
    while q:
        # 현재 원
        n = q.popleft()
        # 현재 원까지의 이동 거리
        d = dist[n]

        # 연결된 원 탐색
        for nn in connect[n]:
            # 방문 체크
            if visited[nn]:
                continue

            visited[nn] = 1
            dist[nn] = d + 1
            q.append(nn)

    return max(dist)

#########################################################################################################################

# 원 개수
N = int(input())

# 원 좌표, 반지름 (반지름 기준 내림차순 정렬)
circles = [[0, 0, 1100000]] + sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:-x[2])

# 원을 트리 구조로 나타냈을 때, 연결 정보 (좌표 평면: 0)
connect = [list() for _ in range(N + 1)]

# 각 원의 트리에서의 레벨 (좌표평면: 0)
level = [0] * (N + 1)

# 가장 높은 레벨과 그 원
max_level, max_circle = 0, 0

# 원 하나씩 트리에 붙이기
for idx in range(1, N + 1):
    # 현재 원 정보
    x, y, R = circles[idx]

    tree(0, -1)

# 하나의 원에서 다른 원으로 이동할 때 방문한 원의 최대 개수
# = 가장 레벨이 높은 리프 노드에서 다른 노드까지의 최대 거리
print(get_dist(max_circle))