from collections import deque
import sys
input = sys.stdin.readline

# W: 지도의 가로 길이, H: 지도의 세로 길이
W, H = map(int, input().split())

# 지도 입력받기
graph = [input().rstrip() for _ in range(H)]

# 레이저의 위치
laser = []
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'C':
            laser.append((i, j))

# 각 칸마다 사용한 거울의 최소 개수
cnt = [[0] * W for _ in range(H)]

# 사방 탐색용
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 현재 위치 정보가 담긴 큐
q = deque()
q.append((laser[0][0], laser[0][1]))

# C에 도착할 때까지 반복
while q:
    # 현재 위치
    r, c = q.popleft()

    # 도착한 경우 끝내기
    if r == laser[1][0] and c == laser[1][1]:
        break

    # 사방 탐색
    for i in range(4):
        # 다음 위치
        nr = r + dr[i]
        nc = c + dc[i]

        # 현재 방향으로 직진
        while True:
            # 범위를 넘어가는 경우 직진 끝내기
            if nr < 0 or nr >= H or nc < 0 or nc >= W:
                break

            # 벽이 나오면 직진 끝내기
            if graph[nr][nc] == '*':
                break

            # 이미 방문한 곳은 넘어가기
            if cnt[nr][nc]:
                nr += dr[i]
                nc += dc[i]
                continue

            # 직진하기 전에 회전했으므로 거울 개수 +1
            # 거울 개수 갱신 후 큐에 넣기
            cnt[nr][nc] = cnt[r][c] + 1
            q.append((nr, nc))

            # 직진
            nr += dr[i]
            nc += dc[i]

# 직진 전에 한 번 회전했다고 가정함
# 출발지에서는 회전하지 않으므로 1 빼주기
print(cnt[laser[1][0]][laser[1][1]] - 1)
