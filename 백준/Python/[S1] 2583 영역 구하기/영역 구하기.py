import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 현재 인접한 영역의 넓이 구하기
def dfs(r, c):
    global N, M, area

    # 넓이 추가
    area += 1

    # 사방 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc]:
            grid[nr][nc] = 0
            dfs(nr, nc)

###############################################################

# 모눈종이 세로, 가로 길이, 직사각형 개수
N, M, K = map(int, input().split())

# 모눈종이
grid = [[1] * M for _ in range(N)]
for _ in range(K):
    # 직사각형 왼쪽 상단, 오른쪽 하단 위치
    lc, lr, rc, rr = map(int, input().split())

    # 직사각형 내부 0으로 채우기
    for i in range(lr, rr):
        for j in range(lc, rc):
            grid[i][j] = 0

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 분리된 영역 구하기
parts = []
for i in range(N):
    for j in range(M):
        if grid[i][j]:
            grid[i][j] = 0

            # 현재 영역의 넓이
            area = 0
            dfs(i, j)
            parts.append(area)

parts.sort()
print(len(parts))
print(*parts)