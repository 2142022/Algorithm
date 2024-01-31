import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 현재 위치에서 사방의 안전 영역 탐색
def dfs(r, c, h):
    # 사방 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and H[nr][nc] > h:
            visited[nr][nc] = 1
            dfs(nr, nc, h)

##########################################################################################3

global N

# 지역 크기
N = int(input())

# 높이 정보
H = []
# 높이 종류
H_set = set()
for _ in range(N):
    info = list(map(int, input().split()))
    H.append(info)
    H_set.update(info)

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 물에 잠기지 않는 안전한 영역의 최대 개수
max_cnt = 1

# 물에 잠기는 높이 기준
for h in H_set:
    # 물에 잠기지 않는 안전한 영역 개수
    cnt = 0

    # 방문 체크
    visited = [[0] * N for _ in range(N)]

    # 한 칸씩 탐색
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and H[i][j] > h:
                cnt += 1
                visited[i][j] = 1
                dfs(i, j, h)

    # 안전 영역 개수 비교
    max_cnt = max(max_cnt, cnt)

print(max_cnt)