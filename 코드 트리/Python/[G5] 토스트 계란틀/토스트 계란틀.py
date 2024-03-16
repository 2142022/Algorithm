from collections import deque
import sys
input = sys.stdin.readline

# (r, c)에서부터 계란 이동
def move(r, c):
    # 계란 이동이 일어날 곳의 위치
    pos = [(r, c)]
    visited[r][c] = 1

    # 계란 이동이 일어날 곳의 계란의 합
    total = board[r][c]

    # 탐색 위치를 담을 큐
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()

        # 현재 위치의 계란 양
        egg = board[r][c]

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue

            # 계란 이동 범위 체크
            negg = board[nr][nc]
            if L <= abs(negg - egg) <= R:
                visited[nr][nc] = 1
                pos.append((nr, nc))
                total += negg
                q.append((nr, nc))

    # 계란 이동이 일어날 수 있는 경우
    if len(pos) > 1:
        # 이동 후의 계란 양
        egg = total // len(pos)
        for r, c in pos:
            board[r][c] = egg
        return 1
    else:
        return 0

################################################################################

# 격자 크기, 계란 이동 범위
N, L, R = map(int, input().split())

# 계란 양
board = [list(map(int, input().split())) for _ in range(N)]

# 계란 이동 횟수
T = 0
while True:
    # 방문 체크
    visited = [[0] * N for _ in range(N)]

    # 계란 이동을 했는지 확인
    flag = 0

    # 계란 이동
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flag |= move(i, j)

    # 더 이상이 이동이 안 일어나는 경우 끝내기
    if not flag:
        break
    T += 1

print(T)
