from collections import deque
import sys
input = sys.stdin.readline

# 목적지(마지막 칸)까지 지나야 하는 최소 칸 수 구하기
def bfs():
    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 현재 위치를 담은 큐
    q = deque([(0, 0)])
    while q:
        # 현재 위치
        r, c = q.popleft()

        # 현재 위치까지의 거리
        cnt = maze[r][c]

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 아직 방문하지 않은 경우 방문
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 0:
                # 목적지인 경우 끝내기
                if nr == N - 1 and nc == M - 1:
                    return cnt + 1

                # 거리 갱신
                maze[nr][nc] = cnt + 1
                q.append((nr, nc))

##############################################################################################

global N, M
# 미로 크기
N, M = map(int, input().split())

# 미로 (이동할 수 있는 칸: 0, 이동할 수 없는 칸: -1)
maze = [list(map(lambda x: {'1': 0, '0': -1}[x], input().rstrip())) for _ in range(N)]
maze[0][0] = 1

# BFS로 마지막 위치까지 이동하기
print(bfs())