from collections import deque
import sys
input = sys.stdin.readline

# 지도 크기
n, m = map(int, input().split())

# 목표 지점
sr = sr = -1

# 지도
board = []
for i in range(n):
    row = list(map(lambda x: -1 if int(x) == 1 else int(x), input().split()))
    board.append(row)
    if sr == -1:
        for j, c in enumerate(row):
            if c == 2:
                sr, sc = i, j
board[sr][sc] = 0

# 목표 지점으로부터의 거리 구하기
q = deque([(sr, sc)])
while q:
    # 탐색 위치
    r, c = q.popleft()

    # 현재 위치까지의 거리
    d = board[r][c]

    # 사방 탐색
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == -1:
            board[nr][nc] = d + 1
            q.append((nr, nc))

for i in board:
    print(*i)