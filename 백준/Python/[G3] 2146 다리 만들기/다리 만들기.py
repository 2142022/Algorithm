from collections import deque
import sys
input = sys.stdin.readline

# 섬 위치 및 개수 확인하기
def check():
    # 섬 번호
    idx = 0

    # 섬 시작점
    for i in range(N):
        for j in range(N):
            if board[i][j] == -1:
                pos.append((i, j))
                board[i][j] = idx

                # 탐색 위치를 담은 큐
                q = deque([(i, j)])
                while q:
                    # 탐색 위치
                    r, c = q.popleft()

                    # 사방 탐색
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == -1:
                            board[nr][nc] = idx
                            q.append((nr, nc))

                # 섬 번호 증가
                idx += 1

    return idx

####################################################################################################

# 현재 섬 idx에서 다른 두 섬까지 놓을 수 있는 다리 중 최소 길이 구하기
def bridge(idx):
    global ML

    # 탐색 시작 위치 (섬 idx 영역 중 한 곳)
    sr, sc = pos[idx]

    # 방문 체크 (섬idx로부터의 거리)
    visited = [[2 * N] * N for _ in range(N)]
    visited[sr][sc] = 0

    # 탐색 위치 및 섬idx로부터의 거리를 담은 큐
    q = deque([(sr, sc, 0)])
    while q:
        # 현재 위치, 섬idx로부터의 거리
        r, c, l = q.popleft()

        # 기존 거리 체크
        if visited[r][c] < l:
            continue

        # 최소 다리 길이보다 큰 경우 패스
        if l >= ML:
            continue

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 기존 거리보다 큰 경우 패스
            if visited[nr][nc] <= l + 1:
                continue

            # 탐색할 위치 정보
            info = board[nr][nc]

            # 섬 idx인 경우
            if info == idx:
                q.append((nr, nc, 0))
                visited[nr][nc] = 0

            # 바다인 경우
            elif info == -2:
                q.append((nr, nc, l + 1))
                visited[nr][nc] = l + 1

            # 다른 섬인 경우
            else:
                # 최소 다리 길이 비교
                if L[idx][info] > l:
                    L[idx][info] = L[info][idx] = l
                    ML = min(ML, l)

####################################################################################################

# 지도 크기
N = int(input())

# 지도 (섬: -1, 바다: -2)
board = [list(map(lambda x: int(x) - 2, input().split())) for _ in range(N)]

# 섬들의 시작점
pos = []

# 섬 위치 및 개수 확인하기
M = check()

# 최소 다리 길이
ML = 2 * N

# 섬i부터 섬j까지 놓은 다리의 최소 길이
L = [[2 * N] * M for _ in range(M)]

# 섬 i에서 놓을 수 있는 최소 다리 길이
for i in range(M - 1):
    bridge(i)

print(ML)