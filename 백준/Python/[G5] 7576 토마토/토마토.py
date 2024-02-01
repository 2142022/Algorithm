from collections import deque
import sys
input = sys.stdin.readline

# BFS로 모든 토마토가 익는 최소 날 수 구하기
def bfs(N, M, remain):
    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 모든 토마토가 익는 최소 날 수
    min_day = 0

    # 익은 토마토 하나씩 꺼내기
    while q:
        # 토마토 위치, 익는데 걸린 날 수
        r, c, day = q.popleft()
        min_day = day

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 아직 안 익은 경우
            if 0 <= nr < N and 0 <= nc < M and tomatoes[nr][nc] == 0:
                remain -= 1
                tomatoes[nr][nc] = 1
                q.append((nr, nc, day + 1))

    # 모든 토마토가 익지 못한 경우 -1 반환
    if remain != 0:
        return -1
    return min_day

##############################################################################

# 상자 크기
M, N = map(int, input().split())

# 토마토 정보
tomatoes = []
# 익지 않은 토마토의 개수
remain = 0
# 익은 토마토의 위치와 그 토마토가 익는데 걸린 날 수를 담은 큐
q = deque()
for i in range(N):
    row = list(map(int, input().split()))
    tomatoes.append(row)
    for j in range(M):
        if row[j] == 0:
            remain += 1
        elif row[j] == 1:
            q.append((i, j, 0))

# 처음부터 모든 토마토가 익어있는 경우
if remain == 0:
    print(0)

# BFS로 모든 토마토가 익는 최소 날 수 구하기
else:
    print(bfs(N, M, remain))