from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

# 불이 퍼지지 않는 영역 크기 구하기
def get_area():
    # 불이 퍼지지 않는 영역
    area = n * m - cnt

    # 방문 체크
    visited = [[0] * m for _ in range(n)]
    for i, j in start:
        visited[i][j] = 1
        area -= 1

    # 탐색 위치를 담은 큐
    q = deque(start)
    while q:
        r, c = q.popleft()

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < n and 0 <= nc < m):
                continue

            # 방문 체크
            if not visited[nr][nc] and board[nr][nc] == 0:
                visited[nr][nc] = 1
                area -= 1
                q.append((nr, nc))

    return area

#######################################################################

# 영역 크기
n, m = map(int, input().split())

# 영역
board = []

# 불의 시작 지점
start = []

# 방화벽을 추가로 설치할 수 있는 위치
pos = []

# 총 방화벽 개수
cnt = 3
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j, c in enumerate(row):
        if c == 0:
            pos.append((i, j))
        elif c == 2:
            start.append((i, j))
        else:
            cnt += 1

# 불이 퍼지지 않는 최대 영역 크기
max_area = 0

# 새로 추가할 방화벽 위치 고르기
for plus in combinations(pos, 3):
    # 방화벽 설치
    for i, j in plus:
        board[i][j] = 1

    # 현재 상태에서 불이 퍼지지 않는 영역 크기 구하기
    max_area = max(max_area, get_area())

    # 방화벽 설치 취소
    for i, j in plus:
        board[i][j] = 0

print(max_area)