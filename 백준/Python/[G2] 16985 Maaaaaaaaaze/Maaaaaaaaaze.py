from collections import defaultdict, deque
from itertools import permutations
import sys
input = sys.stdin.readline

# 입구나 출구가 있는지 확인
# b: 입구나 출구가 있는 판
def check(b):
    for r, c in ((0, 0), (0, 4), (4, 0), (4, 4)):
        if b[r][c] != 0:
            return True
    return False

######################################################################################################################################

# 탈출 시, 최소 이동 횟수 구하기
# 탈출 불가능 시, 갈 수 있는 위치 중 아래 판 구하기
def get_cnt(maze, sr, sc):
    # 방문 체크
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][sr][sc] = 1

    # 제일 아래로 이동했을 때의 판
    bottom = 0

    # 탐색 위치와 현재까지의 이동 횟수를 담은 큐
    q = deque([(0, sr, sc, 0)])
    while q:
        # 현재 위치, 현재까지의 이동 횟수
        i, r, c, t = q.popleft()
        bottom = max(bottom, i)

        # 6방 탐색
        for ni, nr, nc in ((i - 1, r, c), (i + 1, r, c), (i, r - 1, c), (i, r + 1, c), (i, r, c - 1), (i, r, c + 1)):
            # 범위 체크
            if not (0 <= ni < 5 and 0 <= nr < 5 and 0 <= nc < 5):
                continue

            # 갈 수 없는 칸이거나 방문한 곳은 패스
            if maze[ni][nr][nc] == 0 or visited[ni][nr][nc]:
                continue
            visited[ni][nr][nc] = 1

            # 도착 지점에 도착한 경우 끝내기
            if (ni, nr, nc) == (4, 4 - sr, 4 - sc):
                return True, t + 1

            # 다음 위치 큐에 추가
            q.append((ni, nr, nc, t + 1))

    return False, bottom

######################################################################################################################################

# 미로 입구 정하기
# 현재 미로에서 가장 아래로 갔을 때 판 반환
def set_start(maze):
    global escape

    # 탈출 시, 최소 이동 횟수 구하기
    # 탈출 불가능 시, 갈 수 있는 위치 중 아래 판 구하기
    bottom = 0

    for sr, sc in ((0, 0), (0, 4), (4, 0), (4, 4)):
        # 입구가 막혀있는 경우 패스
        if maze[0][sr][sc] == 0:
            continue

        res = get_cnt(maze, sr, sc)
        if res[0]:
            escape = min(escape, res[1])
            bottom = 4
        else:
            bottom = max(bottom, res[1])

    return bottom

######################################################################################################################################

# 판 하나씩 회전하면서 미로 모양 정하기
# order: 판의 순서
# idx: 판 번호
def dfs(order, idx):
    # 최소 이동 횟수가 12인 경우 끝내기
    if escape == 12:
        return

    # 마지막 판까지 모두 정해지면, 현재 미로에서 탈출시키기
    if idx == 5:
        # 현재 미로
        maze = [tuple(board[(i, rot[i])]) for i in order]

        # 이미 확인한 미로는 패스
        if tuple(maze) in maze_set:
            return 5
        maze_set.add(tuple(maze))

        # 현재 미로에서 탈출할 수 있다면 최소 이동 횟수 구하기
        # 현재 미로에서 가장 아래로 갔을 때의 판
        bottom = set_start(maze)

        # 갈 수 없었던 최소 번호의 판으로 돌아가기
        return bottom + 1

    # 현재 판 회전 횟수
    for i in range(4):
        rot[order[idx]] = i

        # 갈 수 없었던 최소 번호의 판
        bottom = dfs(order, idx + 1)
        if bottom == None:
            continue
        if bottom < 5 and idx > bottom:
            return bottom

##############################################################################

# 5X5판 5개를 모두 회전한 모양
# board[(i, j)] : i번째 판을 j번 회전했을 때 모양
board = defaultdict(list)
for i in range(5):
    b = [tuple(map(int, input().split())) for _ in range(5)]
    board[(i, 0)] = b

    # 3번 회전하기 (시계 방향)
    for j in range(1, 4):
        board[(i, j)] = list(map(tuple, zip(*board[(i, j - 1)][::-1])))

# 탈출 최소 이동 횟수
escape = 1000

# 탐색 시 판마다 회전 상태
rot = [0] * 5

# 확인한 미로 모양 체크
maze_set = set()

# 판의 순서 정하기
for order in permutations(range(5), 5):
    # 입구와 출구가 모두 있는지 확인
    if not check(board[(order[0], 0)]) or not check(board[(order[4], 0)]):
        continue

    # 미로 모양 정하기
    dfs(order, 0)

# 탈출할 수 있는 경우
if escape != 1000:
    print(escape)
else:
    print(-1)
