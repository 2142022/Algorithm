import sys
input = sys.stdin.readline

# BFS 사용하여 미로 탐색
def bfs(r, c):
    tmp = []
    tmp.append([r, c])
    cnt[r][c] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # tmp 원소가 없어질 때까지 반복
    while tmp:
        # 첫 번째 원소 pop
        tmp_r, tmp_c = tmp.pop(0)

        for i in range(4):
            nr = tmp_r + dr[i]
            nc = tmp_c + dc[i]
            
            if (nr == N - 1) and (nc == M - 1):
                return cnt[tmp_r][tmp_c] + 1
            
            if (0 <= nr < N) and (0 <= nc < M) and (maze[nr][nc] == 1):
                # cnt가 0이면 아직 방문하지 않았음을 의미
                if cnt[nr][nc] == 0:
                    tmp.append([nr, nc])
                    cnt[nr][nc] = cnt[tmp_r][tmp_c] + 1

# 미로 크기: N X M
N, M = map(int, input().split())

# 미로 입력받기 (strip: 마지막 개행 제거하기 위해 사용)
maze = [list(map(int, input().strip())) for i in range(N)]

# r, c행까지 갈 때까지 지나는 횟수
cnt = [[0] * M for i in range(N)]

print(bfs(0, 0))
