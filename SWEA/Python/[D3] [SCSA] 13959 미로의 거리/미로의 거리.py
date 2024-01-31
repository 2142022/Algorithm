from collections import deque

# BFS로 출발지에서부터 목적지까지의 거리 구하기
def bfs(sr, sc):
    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 출발지로부터의 거리
    dist = [[0] * N for _ in range(N)]

    # 현재 위치를 담은 큐
    q = deque([(sr, sc)])
    while q:
        # 현재 위치
        r, c = q.popleft()

        # 현재까지의 이동 칸 수
        cnt = dist[r][c]

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 아직 방문하지 않은 경우 방문
            if 0 <= nr < N and 0 <= nc < N and not dist[nr][nc] and maze[nr][nc] != 1:
                # 도착지인 경우 끝내기
                if maze[nr][nc] == 3:
                    return cnt

                # 거리 갱신
                dist[nr][nc] = cnt + 1

                # 다음 위치 큐에 넣기
                q.append((nr, nc))

    # 도착지까지 도착할 수 없는 경우
    return 0

#####################################################################################################

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    global N

    # 미로 크기
    N = int(input())

    # 미로
    maze = []
    # 출발지
    sr = sc = 0
    for i in range(N):
        info = list(map(int, input()))
        maze.append(info)
        for j, num in enumerate(info):
            if num == 2:
                sr, sc = i, j

    # BFS로 출발지에서부터 목적지까지의 거리 구하기
    print(f'#{t} {bfs(sr, sc)}')

