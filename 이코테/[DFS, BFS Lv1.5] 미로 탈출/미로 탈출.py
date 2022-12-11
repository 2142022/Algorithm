from collections import deque
import sys
input = sys.stdin.readline

# BFS로 칸 세기
# q: 위치 정보가 담긴 큐
def escape(q):
    # N, M: 전역 변수
    global N, M

    # 사방 탐색을 위한 배열
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 큐에 원소가 없어질 때까지 반복
    while q:
        # 현재 위치 뽑기
        r, c = q.popleft()

        # 사방 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 미로의 출구에 도착했다면 끝내기
            # 반환값은 현재 위치까지의 칸 수 + 1
            if nr == N - 1 and nc == M - 1:
                return cnt[r][c] + 1

            # 미로 범위를 벗어났다면 패스
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 괴물이 있는 곳이거나 이미 방문한 곳이면 패스
            if maze[nr][nc] == 0 or cnt[nr][nc] != 0:
                continue

            # 큐에 탐색 위치 넣고 방문 체크(칸 수 바꾸기)
            q.append([nr, nc])
            cnt[nr][nc] = cnt[r][c] + 1

############################################################

# 미로 크기: N X M
N, M = map(int, input().split())

# 미로 정보
maze = [list(map(int, input().strip())) for _ in range(N)]

# 큐에 시작 위치((0, 0)) 담기
q = deque()
q.append([0, 0])

# cnt[i][j] = (i, j)까지 이동한 칸 수
cnt = [[0] * M for _ in range(N)]
# 시작 위치까지의 칸 수는 1
cnt[0][0] = 1

# BFS로 미로 탈출까지의 최소 칸 수 구하고 출력
print(escape(q))