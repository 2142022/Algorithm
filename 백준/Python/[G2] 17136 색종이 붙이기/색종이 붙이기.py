import sys
input = sys.stdin.readline

# 현재 크기의 색종이를 둘 수 있는지 여부와 색종이를 두고 난 후의 종이
# paper: 현재 종이 정보
# size: 두려고 하는 색종이 크기
# r, c: 색종이를 둘 시작점
def is_possible(paper, size, r, c):
    # 색종이 두기
    for i in range(r, r + size):
        for j in range(c, c + size):
            if i >= 10 or j >= 10:
                return 0, 0
            if not paper & 1 << (10 * i + j):
                return 0, 0
            paper &= ~(1 << (10 * i + j))
    return 1, paper

############################################################################

# DFS로 색종이 두기
# cnt: 현재까지 둔 색종이 개수
# paper: 현재 종이 정보
# limit: 현재 색종이를 놓을 수 있는 칸의 개수
def dfs(cnt, paper, limit):
    global min_cnt

    # 더 이상 색종이를 놓을 수 있는 칸이 없는 경우 끝내기
    if limit == 0:
        min_cnt = min(min_cnt, cnt)
        return

    # 현재까지 둔 색종이의 개수가 최소 색종이 개수 이상인 경우 끝내기
    if cnt >= min_cnt:
        return

    # 남은 색종이가 없는 경우 끝내기
    if sum(colors) == 0:
        return

    # 색종이를 둘 수 있는 최초 위치
    r, c = divmod(len(bin(paper)) - bin(paper).rindex('1') - 1, 10)

    # 색종이 크기
    for size in range(1, 6):
        # 현재 크기의 색종이가 없는 경우 패스
        if colors[size] == 0:
            continue

        # 현재 크기의 색종이를 둘 수 있는지 여부와 색종이를 두고 난 후의 종이
        possible, p = is_possible(paper, size, r, c)
        if not possible:
            continue

        # 다음 위치 탐색
        colors[size] -= 1
        dfs(cnt + 1, p, limit - size ** 2)
        colors[size] += 1

############################################################################

# 종이 (비트마스킹)
paper = 0
# 색종이를 놓을 수 있는 칸의 개수
limit = 0
for i in range(10):
    info = list(map(int, input().split()))
    for j in range(10):
        if info[j]:
            limit += 1
            paper |= 1 << (10 * i + j)

# 색종이의 최소 개수
min_cnt = 100

# 남은 색종이 개수
colors = [5] * 6

# DFS로 색종이 두기
dfs(0, paper, limit)

# 칸을 모두 채울 수 없는 경우
if min_cnt == 100:
    print(-1)
else:
    print(min_cnt)