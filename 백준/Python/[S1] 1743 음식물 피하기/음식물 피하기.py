from collections import deque
import sys
input = sys.stdin.readline

# 통로 크기, 음식물 쓰레기 개수
N, M, K = map(int, input().split())

# 음식물 위치 체크
board = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

# 가장 큰 음식물 쓰레기 크기
max_size = 0

# 음식물 쓰레기 시작점
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if board[i][j]:
            # 음식물 쓰레기 크기
            size = 1

            # 방문 체크
            board[i][j] = 0

            # 탐색 위치를 담은 큐
            q = deque([(i, j)])
            while q:
                # 현재 위치
                r, c = q.popleft()

                # 사방 탐색
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    # 범위 체크
                    if not (0 < nr <= N and 0 < nc <= M):
                        continue

                    # 음식물 쓰레기 체크
                    if board[nr][nc]:
                        q.append((nr, nc))
                        size += 1
                        board[nr][nc] = 0

            max_size = max(max_size, size)

print(max_size)