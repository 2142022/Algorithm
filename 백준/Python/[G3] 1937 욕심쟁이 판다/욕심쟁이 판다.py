import sys
input = sys.stdin.readline

# 현재 위치 (r, c)에서 판다가 이동할 수 있는 최대 칸 수
def go(r, c):
    # 이전에 구한 적이 있는 경우
    if cnt[r][c]:
        return cnt[r][c]

    # 최대 이동 칸 수
    mc = 1

    # 사방 탐색
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if not (0 <= nr < n and 0 <= nc < n):
            continue

        # 현재 위치보다 대나무가 더 많은 곳만 이동 가능
        if forest[nr][nc] > forest[r][c]:
            mc = max(mc, go(nr, nc) + 1)

    cnt[r][c] = mc
    return mc

#######################################################################

# 숲 크기
n = int(input())

# 숲
forest = [list(map(int, input().split())) for _ in range(n)]

# 각 위치에서 판다가 이동할 수 있는 최대 칸 수
cnt = [[0] * n for _ in range(n)]

# 최종적으로 판다가 이동할 수 있는 최대 칸 수
max_cnt = 0

# 출발 위치
for i in range(n):
    for j in range(n):
        max_cnt = max(max_cnt, go(i, j))

print(max_cnt)