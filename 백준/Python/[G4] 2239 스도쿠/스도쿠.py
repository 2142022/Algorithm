import sys
input = sys.stdin.readline

# 현재 위치가 몇 번째 사각형인지 구하기
def find_square(i, j):
    if i < 3:
        if j < 3:
            return 0
        elif j < 6:
            return 1
        else:
            return 2
    elif i < 6:
        if j < 3:
            return 3
        elif j < 6:
            return 4
        else:
            return 5
    else:
        if j < 3:
            return 6
        elif j < 6:
            return 7
        else:
            return 8

#############################################################

# (r, c)에 num을 채울 수 있는지 확인
def possible(r, c, s, num):
    if rows[r] & 1 << num:
        return False
    if cols[c] & 1 << num:
        return False
    if square[s] & 1 << num:
        return False
    return True

#############################################################

# i번째 빈 칸 채우기
def fill(i):
    # 모든 빈 칸을 다 채운 경우 끝내기
    if i == len(empty):
        return 1

    # 현재 위치
    r, c = empty[i]
    s = find_square(r, c)

    # 숫자 채우기
    for num in range(1, 10):
        # 사용 가능한 숫자인지 확인
        if possible(r, c, s, num):
            rows[r] |= 1 << num
            cols[c] |= 1 << num
            square[s] |= 1 << num

            # 숫자 채우기
            board[r][c] = num
            if fill(i + 1):
                return 1

            # 초기화
            rows[r] &= ~(1 << num)
            cols[c] &= ~(1 << num)
            square[s] &= ~(1 << num)

    return 0

#############################################################

# 보드
board = []

# 빈 칸 위치
empty = []

# 각 행, 열, 사각형별 사용한 숫자 체크
rows = [0] * 9
cols = [0] * 9
square = [0] * 9

# 입력받기
for i in range(9):
    row = list(map(int, input().rstrip()))
    board.append(row)
    for j, num in enumerate(row):
        if num == 0:
            empty.append((i, j))
        else:
            rows[i] |= 1 << num
            cols[j] |= 1 << num
            square[find_square(i, j)] |= 1 << num

# 빈 칸 하나씩 채우기
fill(0)

# 보드 출력
for b in board:
    print(''.join(map(str, b)))