import sys
input = sys.stdin.readline

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

# 한 곳씩 십자가 두기
def put():
    # 십자가 위치, 크기
    result = []

    # 십자가를 둘 위치
    for r, c in pos:
        # 십자가의 최대 크기
        # 겹쳐서 놓아도 되므로 최대 크기로 두기
        s = get_size(r, c)

        # 십자가를 둘 수 없는 경우 패스
        if s == 0:
            continue

        # 십자가 위치, 크기 추가
        result.append((r + 1, c + 1, s))

        # 십자가 두기
        board[r][c] += 1
        for i in range(1, s + 1):
            board[r - i][c] += 1
            board[r + i][c] += 1
            board[r][c - i] += 1
            board[r][c + i] += 1

    return result

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
    # 십자가 위치, 크기 구하기
    result = put()

    # 만약, 십자가로 격자판을 만들 수 없는 경우 -1 출력
    if not finish():
        print(-1)

    # 십자가 개수, 위치, 크기 출력
    else:
        print(len(result))
        for i in result:
            print(*i)