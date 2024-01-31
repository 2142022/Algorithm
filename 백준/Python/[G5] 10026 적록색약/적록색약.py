import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 한 구역 탐색하기
# r, c: 현재 위치
# color: 현재 위치의 색깔
def dfs(r, c, color):
    # 현재 위치가 초록색인 경우 빨간색으로 바꾸기 (1 -> 0)
    if grid[r][c] == 1:
        grid[r][c] = 0

    # 사방 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        # 같은 색깔 탐색
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == color:
            visited[nr][nc] = 1
            dfs(nr, nc, color)

######################################################################################################

# 구역 개수 구하기
def get_cnt():
    global visited

    # 방문체크
    visited = [[0] * N for _ in range(N)]

    # 구역 개수
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                cnt += 1
                dfs(i, j, grid[i][j])

    return cnt

######################################################################################################

global N

# 그리드 크기
N = int(input())

# 그리드 (빨강 - 0, 초록 - 1, 파랑 - 2)
grid = [list(map(lambda x: {'R': 0, 'G': 1, 'B': 2}[x], input().rstrip())) for _ in range(N)]

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 적록색약이 아닌 사람이 봤을 때, 적록색약인 사람이 봤을 때의 구역 개수 구하기
print(get_cnt(), get_cnt())