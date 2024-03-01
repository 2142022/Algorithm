import sys
input = sys.stdin.readline

# 출발 위치나 도착 위치인 경우, 이미 가스관과 연결되어 있는지 확인
def connect(r, c):
    # 사방 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        # 범위 체크
        if not (0 <= nr < R and 0 <= nc < C):
            continue

        # 다른 가스관이 있는 경우
        if board[nr][nc] > 0:
            return True

    return False

#############################################################################################################################################################

# (r, c)에 필요한 블록 모양 찾기
def get_shape(r, c):
    # 사방에 블록의 필요 여부
    flag = [0] * 4

    # 사방 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        # 범위 체크
        if not (0 <= nr < R and 0 <= nc < C):
            continue

        # 가스관이나 도착 위치, 출발 위치가 있는 경우
        s = abs(board[nr][nc])

        # 출발 위치나 도착 위치인 경우, 이미 다른 가스관과 연결되었다면 패스
        if s == 100 and not connect(nr, nc):
            flag[d] = 1

        # (r, c)로 이어진 방향이 있는 경우, 블록 필요
        elif 0 < s < 100 and (d + 2) % 4 in need[s]:
            flag[d] = 1

    # 빠진 블록의 위치가 아닌 경우
    if sum(flag) == 0:
        return 0

    # 빠진 블록의 위치인 경우 필요한 블록
    blocks = {(0, 1, 1, 0): 1, (1, 1, 0, 0): 2, (1, 0, 0, 1): 3, (0, 0, 1, 1): 4, (1, 0, 1, 0): 5, (0, 1, 0, 1): 6, (1, 1, 1, 1): 7}
    return blocks[tuple(flag)]

#############################################################################################################################################################

# 유럽 크기
R, C = map(int, input().split())

# 출발 위치
sr = sc = -1

# 유럽
board = []
for i in range(R):
    row = list(map(lambda x: {'.': 0, '1': 1, '2': 2, '3': 3, '4': 4, '|': 5, '-': 6, '+': 7, 'M': 100, 'Z': -100}[x], input().rstrip()))
    board.append(row)
    if sr == -1:
        for j, c in enumerate(row):
            if c == 100:
                sr, sc = i, j
                break

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 모양별로 필요한 방향 저장
need = {1: (1, 2), 2: (0, 1), 3: (0, 3), 4: (2, 3), 5: (0, 2), 6: (1, 3), 7: (0, 1, 2, 3), 100: (0, 1, 2, 3)}

r = c = -1
shape = ''

# 빈 칸인 곳
for i in range(R):
    for j in range(C):
        if board[i][j] == 0:
            # 현재 위치에 필요한 블록 모양 찾기
            s = get_shape(i, j)
            if s:
                r, c = i + 1, j + 1
                if s == 5:
                    shape = '|'
                elif s == 6:
                    shape = '-'
                elif s == 7:
                    shape = '+'
                else:
                    shape = str(s)

            if r != -1:
                break

    if r != -1:
        break

print(r, c, shape)