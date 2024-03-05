from collections import deque
import sys
input = sys.stdin.readline

# 각 위치에서 유령에게 발견되는 시간 저장하기
def get_discover():
    # 유령 위치
    for r, c in ghost:
        # 처음 유령 방향
        d = board[r][c]

        # 사방 탐색
        for t in range(4):
            nr, nc = r + dr[d], c + dc[d]
            while 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 100:
                discover[t][nr][nc] = 1
                nr += dr[d]
                nc += dc[d]
            d = (d + 1) % 4

#################################################################################################################

# 유령의 집을 탈출하는 데 걸리는 최소 시간 구하기
def escape():
    # 같은 시간대(나머지가 같은 시간) 방문 체크
    time = [[0] * M for _ in range(N)]
    time[sr][sc] = 1 << 0

    # 탐색 위치, 시간을 담은 큐
    q = deque([(sr, sc, 0)])
    while q:
        # 현재 위치, 현재까지 걸린 시간
        r, c, t = q.popleft()

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 빈 공간만 이동 가능
            if board[nr][nc] != 100:
                continue

            # 다음 위치까지 가는데 걸리는 시간의 나머지
            nm = (t + 1) % 4

            # 다음 위치 방문 체크
            if time[nr][nc] & 1 << nm:
                continue

            # 유령에게 발견되는 경우 대기
            if discover[nm][nr][nc]:
                if not time[r][c] & 1 << nm and not discover[nm][r][c]:
                    time[r][c] |= 1 << nm
                    q.append((r, c, t + 1))

            # 다음 위치 이동
            else:
                # 도착 지점인 경우 끝내기
                if nr == er and nc == ec:
                    return t + 1
                time[nr][nc] |= 1 << nm
                q.append((nr, nc, t + 1))

    # 유령에게 발견되지 않고 탈출하는 방법이 없는 경우
    return 'GG'

#################################################################################################################

# 유령의 집 크기
N, M = map(int, input().split())

# 입구, 출구
sr, sc, er, ec = map(lambda x: int(x) - 1, input().split())

# 유령의 집
board = []
# 유령의 위치
ghost = []
for i in range(N):
    row = list(map(lambda x: {'#': -1, '.': 100, '0': 0, '1': 1, '2': 2, '3': 3}[x], input().rstrip()))
    board.append(row)
    for j, info in enumerate(row):
        if 0 <= info <= 3:
            ghost.append((i, j))

# 사방 탐색용 (오, 하, 왼, 상)
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

# discover[k][i][j]: 나머지가 k인 시간에 (i, j)에 있으면 유령에게 발견됨을 의미
discover = [[[0] * M for _ in range(N)] for _ in range(4)]
get_discover()

# 유령의 집을 탈출하는 데 걸리는 최소 시간
print(escape())
