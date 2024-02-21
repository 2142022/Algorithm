import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 현재 위치 (r, c)에서 둘 수 있는 십자가 최대 크기 구하기
def get_size(r, c):
    s = 1
    while True:
        if r - s < 0 or board[r - s][c] == 0:
            return s - 1
        elif r + s >= N or board[r + s][c] == 0:
            return s - 1
        elif c - s < 0 or board[r][c - s] == 0:
            return s - 1
        elif c + s >= M or board[r][c + s] == 0:
            return s - 1
        s += 1

################################################################################

# 격자판이 완성됐는지 확인
def finish():
    for i, j in pos:
        if board[i][j] == 1:
            return 0
    return 1

################################################################################

# idx번째로 십자가를 둘 수 있는 곳에 십자가 두기
# cnt: 현재까지 둔 십자가의 개수
def put(idx, cnt):
    # 모든 곳에 십자가를 다 둔 경우 끝내기
    if idx == len(pos):
        # 격자판이 완성됐는지 확인
        if finish():
            print(cnt)
            return 1
        return 0

    # 현재 위치
    r, c = pos[idx]

    # 둘 수 있는 십자가 최대 크기
    # 겹쳐서 둘 수 있으므로 최대 크기로 두기
    s = get_size(r, c)

    # 십자가를 둘 수 없는 경우, 다음 위치 탐색
    if s == 0:
        if put(idx + 1, cnt):
            return 1
        return 0

    # 십자가 두기
    board[r][c] += 1
    for i in range(1, s + 1):
        board[r - i][c] += 1
        board[r + i][c] += 1
        board[r][c - i] += 1
        board[r][c + i] += 1

    # 격자판을 완성한 경우 끝내기
    if put(idx + 1, cnt + 1):
        print(r + 1, c + 1, s)
        return 1

    # 격자판을 완성하지 못하는 경우 끝내기
    else:
        return 0

################################################################################

# 격자판 크기
N, M = map(int, input().split())

# 격자판
board = []

# 십자가의 중심이 될 수 있는 곳의 위치
pos = []
for i in range(N):
    row = list(map(lambda x: 1 if x == '*' else 0, input().rstrip()))
    board.append(row)
    for j in range(M):
        if row[j]:
            pos.append((i, j))

# 십자가를 둘 필요가 없는 경우
if len(pos) == 0:
    print(0)

# 한 곳씩 십자가 두기
else:
    # 만약, 십자가로 격자판을 만들 수 없는 경우 -1 출력
    if not put(0, 0):
        print(-1)