from collections import deque
import sys
input = sys.stdin.readline

# 미로 크기
M, N = map(int, input().split())

# 미로
maze = [list(map(int, input().rstrip())) for i in range(N)]

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 벽을 부순 최소 횟수
cnt = [[-1] * M for i in range(N)]
cnt[0][0] = 0

# 현재 위치를 담은 큐
q = deque([(0, 0)])
while q:
    # 현재 위치
    r, c = q.popleft()

    # 사방 탐색
    for i in range(4):
        # 다음 위치
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위를 벗어나는 경우 패스
        if not (0 <= nr < N and 0 <= nc < M):
            continue

        # 이미 방문한 곳 패스
        if cnt[nr][nc] != -1:
            continue

        # 벽이 있는 경우 벽을 부수고 이동
        if maze[nr][nc]:
            cnt[nr][nc] = cnt[r][c] + 1
            q.append((nr, nc))
        else:
            cnt[nr][nc] = cnt[r][c]
            # 벽이 없는 곳을 먼저 탐색
            q.appendleft((nr, nc))

print(cnt[N - 1][M - 1])