from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 빙산 덩어리 개수 세기 + 빙산의 각 위치에서 사방의 바다 개수 세기
def get_cnt():
    global ocean

    # 빙산의 각 위치에서 사방의 바다 개수 세기
    ocean = defaultdict(int)

    # 빙산 덩어리 개수
    cnt = 0

    # 방문 체크용
    visited = [[0] * M for _ in range(N)]

    # 빙산 덩어리 시작점
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1

                # BFS로 현재 덩어리 탐색하기
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()

                    # 사방 탐색
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < M:
                            # 바다인 경우
                            if board[nr][nc] == 0:
                                ocean[(r, c)] += 1
                                continue

                            # 방문 체크
                            if visited[nr][nc]:
                                continue
                            visited[nr][nc] = 1
                            q.append((nr, nc))

    return cnt

#########################################################################

global N, M

# 배열 크기
N, M = map(int, input().split())

# 배열
board = [list(map(int, input().split())) for _ in range(N)]

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 빙산이 분리되는 시간
time = 0

# 빙산이 분리될 때까지 반복
while True:
    # 덩어리 개수
    cnt = get_cnt()

    # 덩어리가 0개라면 0 출력
    if cnt == 0:
        print(0)
        break

    # 덩어리가 1개가 아니라면 시간 출력
    if cnt != 1:
        print(time)
        break

    # 시간 증가
    time += 1

    # 빙산 녹이기
    for pos, affect in ocean.items():
        board[pos[0]][pos[1]] = max(0, board[pos[0]][pos[1]] - affect)
