import sys
input = sys.stdin.readline

# (r, c)에서 내리막길로 이동
def dfs(r, c):
    # 목적지인 경우
    if r == N - 1 and c == M - 1:
        cnt[r][c] = 1
        return cnt[r][c]

    # 현재 위치에서 목적지까지 가는 경로의 수를 이미 구한 경우
    # 목적지까지 가는 경로가 없는 경우 -1이므로 0과 비교
    if cnt[r][c]:
        return max(cnt[r][c], 0)

    # 내리막길로 이동
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= nr < N and 0 <= nc < M and H[nr][nc] < H[r][c]:
            cnt[r][c] += dfs(nr, nc)

    # 목적지까지 가는 경로가 없는 경우
    if cnt[r][c] == 0:
        cnt[r][c] = -1
        return 0

    return cnt[r][c]

##########################################################################

# 지도 크기
N, M = map(int, input().split())

# 각 지점의 높이
H = [list(map(int, input().split())) for _ in range(N)]

# 각 지점에서 목적지까지 갈 수 있는 경로의 수
cnt = [[0] * M for _ in range(N)]

# 내리막길 이동
dfs(0, 0)

# 목적지까지 가는 경로가 없는 경우 -1이므로 0과 비교
print(max(cnt[0][0], 0))
