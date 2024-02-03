from collections import deque
import sys
input = sys.stdin.readline

# 최단 경로 구하기
def bfs(N, M, K):
    # 방문 체크 (벽 부순 횟수 저장, 밤낮 체크)
    cnt = [[[K + 1] * M for _ in range(N)] for _ in range(2)]
    cnt[1][0][0] = 0

    # 현재 위치, 이동 횟수, 밤낮을 담은 큐
    q = deque([(0, 0, 1, 1)])
    while q:
        # 현재 위치, 이동 횟수, 밤낮
        r, c, d, f = q.popleft()

        # 현재 위치에서 벽을 부순 최소 횟수
        t = cnt[f][r][c]

        # 밤에는 이동하지 않는 경우 큐에 추가
        # 낮에는 벽이든 통로든 이동 가능하기 때문에 추가하지 않음
        if f == 0 and cnt[f^1][r][c] > t:
            cnt[f^1][r][c] = t
            q.append((r, c, d + 1, f^1))

        # 사방 탐색
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc

            # 도착한 경우 끝내기
            if nr == N - 1 and nc == M - 1:
                return d + 1

            # 범위를 벗어난 곳은 패스
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 벽인 경우 낮에 아직 벽을 부술 수 있다면 이동
            if board[nr][nc] == 1:
                if t < K and f == 1 and cnt[f^1][nr][nc] > t + 1:
                    cnt[f^1][nr][nc] = t + 1
                    q.append((nr, nc, d + 1, f^1))

            # 벽이 아닌 곳은 방문하지 않았거나 기존보다 벽을 부순 횟수가 적다면 탐색
            else:
                if cnt[f^1][nr][nc] > t:
                    cnt[f^1][nr][nc] = t
                    q.append((nr, nc, d + 1, f^1))

    # 끝까지 이동을 못하는 경우
    return -1

################################################################################

# 맵 크기, 벽을 부술 수 있는 최대 횟수
N, M, K = map(int, input().split())

# 맵
board = [list(map(int, input().rstrip())) for _ in range(N)]

# 맵이 한 칸인 경우 1 반환
if N == 1 and M == 1:
    print(1)

# 최단 경로 구하기
else:
    print(bfs(N, M, K))