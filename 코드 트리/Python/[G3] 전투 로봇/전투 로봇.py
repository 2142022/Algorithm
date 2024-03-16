from collections import deque
import sys
input = sys.stdin.readline

# 죽일 몬스터의 위치 찾기
# sr, sc: 현재 전투 로봇의 위치
def find(sr, sc):
    # 방문 체크
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    # 몬스터를 죽이는 최소 시간
    min_time = N * N

    # 죽일 수 있는 몬스터의 위치
    monster = []

    # 탐색 위치, 이동 시간을 담을 큐
    q = deque([(sr, sc, 0)])
    while q:
        r, c, t = q.popleft()

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1

            # 죽일 수 있는 몬스터인 경우
            if 0 < board[nr][nc] < level and t + 1 <= min_time:
                monster.append((nr, nc))
                min_time = t + 1
                continue

            # 지나가기
            if board[nr][nc] <= level and t + 1 < min_time:
                q.append((nr, nc, t + 1))

    # 죽일 수 있는 몬스터의 위치, 시간
    if not monster:
        return -1, -1, -1
    return *sorted(monster, key = lambda x: (x[0], x[1]))[0], min_time

############################################################################

# 격자판 크기
N = int(input())

# 격자판
board = []
# 전투로봇 위치
r, c = -1, -1
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    if r == -1:
        for j, num in enumerate(row):
            if num == 9:
                r, c = i, j
                board[i][j] = 0

# 사방 탐색용 (상, 좌, 우, 하)
dr, dc = (-1, 0, 0, 1), (0, -1, 1, 0)

# 전투 시간, 현재까지 죽인 몬스터 수, 전투로봇 레벨
time, cnt, level = 0, 0, 2
while True:
    # 죽일 몬스터의 위치 찾기
    pr, pc, pt = find(r, c)

    # 없앨 수 있는 몬스터가 없는 경우 끝내기
    if pr == -1:
        break

    # 죽이기
    cnt += 1
    time += pt
    board[pr][pc] = 0
    r, c = pr, pc

    # 레벨만큼 몬스터를 죽였으면 레벨업
    if cnt == level:
        level += 1
        cnt = 0

print(time)