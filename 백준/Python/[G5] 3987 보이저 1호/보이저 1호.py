import sys
input = sys.stdin.readline

# 현재 방향 d에서 행성을 만난 경우
def change_dir(d, planet):
    if planet == '/':
        if d == 0:
            return 1
        if d == 1:
            return 0
        if d == 2:
            return 3
        if d == 3:
            return 2

    else:
        if d == 0:
            return 3
        if d == 1:
            return 2
        if d == 2:
            return 1
        if d == 3:
            return 0

###########################################################################

# (r, c)에서 d 방향으로 시그널을 보냈을 때의 최대 탐색 시간 구하기
def go(r, c, d):
    # 출발 위치부터 블랙홀인 경우
    if board[r][c] == 'C':
        return 0

    # 출발 위치부터 방향을 바꿔야 하는 경우
    if board[r][c] == '/' or board[r][c] == '\\':
        d = change_dir(d, board[r][c])

    # 방문 체크
    visited = [[[0] * M for _ in range(N)] for _ in range(4)]
    visited[d][r][c] = 1

    # 이동 시간
    time = 0

    # 계속 이동
    while True:
        # 다음 위치
        nr, nc = r + dr[d], c + dc[d]

        # 범위를 벗어나거나 블랙홀을 만난 경우
        if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] == 'C':
            return time + 1

        # 이미 방문한 곳인 경우, 무한히 반복됨
        if visited[d][nr][nc]:
            return 1000000

        # 방향을 바꿔야 하는 경우
        if board[nr][nc] == '/' or board[nr][nc] == '\\':
            d = change_dir(d, board[nr][nc])

        # 이동
        visited[d][nr][nc] = 1
        r, c = nr, nc
        time += 1

###########################################################################


# 항성계 크기
N, M = map(int, input().split())

# 항성계
board = [input().strip() for _ in range(N)]

# 출발 위치
PR, PC = map(int, input().split())

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 최대 시간과 그 때의 시그널 초기 방향
max_time, first_dir = -1, 0

# 네 방향으로 모두 보내보기
for i, d in enumerate('URDL'):
    time = go(PR - 1, PC - 1, i)

    # 시그널이 항성계 내에서 무한히 전파될 수 있는 경우
    if time == 1000000:
        max_time = time
        first_dir = d
        break

    # 시간 비교
    if time > max_time:
        max_time = time
        first_dir = d

# 시그널이 항성계 내에서 무한히 전파될 수 있는 경우
print(first_dir)
if max_time == 1000000:
    print("Voyager")
else:
    print(max_time)
