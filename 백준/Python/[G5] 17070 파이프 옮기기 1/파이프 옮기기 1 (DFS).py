import sys
input = sys.stdin.readline

# DFS로 파이프 한 칸씩 이동하기
# r, c: (0, 0)에서 더 먼 파이프의 위치
# d: 파이프가 놓인 방향 (0 - 가로, 1 - 세로, 2 - 대각선)
def dfs(r, c, d):
    global N

    # 파이프가 모두 이동한 경우
    if r == c == N - 1:
        return 1

    # 현재 위치에서 끝까지 이동한 횟수가 기록되어 있는 경우
    if cnt[r][c][d]:
        return cnt[r][c][d]

    # 현재 위치에서 갈 수 있는 경우의 수 더하기
    for nd, s in enumerate(shift[d]):
        if s[0] == -1:
            continue

        nr, nc = r + s[0], c + s[1]
        if 0 <= nr < N and 0 <= nc < N and house[nr][nc] == 0:
            # 대각선으로 이동하기 위해서는 다른 오른쪽, 아래도 빈 칸인지 확인
            if nd == 2 and (house[nr - 1][nc] != 0 or house[nr][nc - 1] != 0):
                continue
            cnt[r][c][d] += dfs(nr, nc, nd)

    return cnt[r][c][d]

#############################################################################

# 집 크기
N = int(input())

# 집
house = [list(map(int, input().split())) for _ in range(N)]

# 도착지점이 1인 경우 이동 불가
if house[-1][-1] == 1:
    print(0)
    exit()

# 파이프의 위치와 파이프가 놓인 방향에 따라 끝까지 이동할 수 있는 방법의 수 저장
# 위치는 (0, 0)에서 더 먼 파이프의 위치
# 방향: 0 - 가로, 1 - 세로, 2 - 대각선
cnt = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 파이프가 놓인 방향에 따라 이동할 수 있는 위치
# 다음 방향은 인덱스로 체크하기 위해서 갈 수 없는 곳은 (-1, -1)로 채워둠
shift = {0: [(0, 1), (-1, -1), (1, 1)], 1: [(-1, -1), (1, 0), (1, 1)], 2: [(0, 1), (1, 0), (1, 1)]}

# DFS로 하나씩 이동하기
print(dfs(0, 1, 0))