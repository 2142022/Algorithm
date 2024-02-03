from collections import deque
import sys
input = sys.stdin.readline

# 최단 경로 구하기
def bfs(N, M):
    # 이동 칸 수 (벽을 부순 여부에 따라 0, 1로 나눔)
    dist = [[[0] * M for _ in range(N)] for _ in range(2)]
    dist[0][0][0] = 1

    # 현재 위치, 벽 부순 여부를 담은 큐
    q = deque([(0, 0, 0)])
    while q:
        # 현재 위치, 벽 부순 여부
        r, c, p = q.popleft()

        # 현재까지 이동 거리
        d = dist[p][r][c]

        # 사방 탐색
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc

            # 도착한 경우 끝내기
            if nr == N - 1 and nc == M - 1:
                return d + 1

            # 범위를 벗어난 곳은 패스
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 벽인 경우 아직 벽을 한번도 안 부셨다면 이동 가능
            if board[nr][nc] == 1:
                if p == 0:
                    dist[1][nr][nc] = d + 1
                    q.append((nr, nc, 1))

            # 벽이 아닌 곳은 방문하지 않았으면 탐색
            else:
                if dist[p][nr][nc] == 0:
                    dist[p][nr][nc] = d + 1
                    q.append((nr, nc, p))

    # 끝까지 이동을 못하는 경우
    return -1

##########################################################################3

# 맵 크기
N, M = map(int, input().split())

# 맵
board = [list(map(int, input().rstrip())) for _ in range(N)]

# 맵이 한 칸인 경우 1 반환
if N == 1 and M == 1:
    print(1)

# 최단 경로 구하기
else:
    print(bfs(N, M))
