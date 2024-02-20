from collections import defaultdict
import sys
input = sys.stdin.readline

# 위치 숫자로 변환
def get_pos(x):
    return ord(x[0]) - ord('A'), int(x[1]) - 1

###########################################################################################################

# (r, c)가 있는 사각형 번호 구학
def get_square(r, c):
    if 0 <= r < 3:
        if 0 <= c < 3:
            return 0
        elif 3 <= c < 6:
            return 1
        else:
            return 2
    elif 3 <= r < 6:
        if 0 <= c < 3:
            return 3
        elif 3 <= c < 6:
            return 4
        else:
            return 5
    else:
        if 0 <= c < 3:
            return 6
        elif 3 <= c < 6:
            return 7
        else:
            return 8

###########################################################################################################

# 행별, 열별, 사각형별 사용한 숫자 체크
# r, c: 위치
# num: 숫자
# flag: 1이면 방문 체크, 0이면 방문 취소
def visit(r, c, num, flag):
    global rows, columns, square

    if flag:
        rows |= 1 << (9 * r + num - 1)
        columns |= 1 << (9 * c + num - 1)
        square |= 1 << (9 * get_square(r, c) + num - 1)

    else:
        rows &= ~(1 << (9 * r + num - 1))
        columns &= ~(1 << (9 * c + num - 1))
        square &= ~(1 << (9 * get_square(r, c) + num - 1))

###########################################################################################################

# (r, c)와 같은 행, 열, 사각형에 같은 숫자가 존재하는지 체크
def is_exist(r, c, num):
    if rows & 1 << (9 * r + num - 1):
        return 1
    if columns & 1 << (9 * c + num - 1):
        return 1
    if square & 1 << (9 * get_square(r, c) + num - 1):
        return 1
    return 0

###########################################################################################################

# idx번째로 비어있는 칸에 숫자 채우기
def fill(idx):
    # 모든 칸을 다 채운 경우 끝내기
    if idx == len(empty):
        return 1

    # 현재 위치
    r, c = empty[idx]

    # 이미 채워진 경우 패스
    if board[r][c]:
        if fill(idx + 1):
            return 1
        return 0

    # 채울 수 있는 숫자 탐색
    for n1 in range(1, 10):
        # 같은 행, 열, 사각형에 같은 숫자가 존재하는지 체크
        if is_exist(r, c, n1):
            continue

        # 도미노 타일의 나머지 위치 (현재 위치의 오른쪽, 아래)
        for nr, nc in ((r, c + 1), (r + 1, c)):
            # 범위 및 이미 채워져 있는지 체크
            if nr >= 9 or nc >= 9 or board[nr][nc]:
                continue

            # 채울 수 있는 숫자 탐색
            for n2 in range(1, 10):
                # n1과 같은 숫자는 패스
                if n1 == n2:
                    continue

                # 같은 행, 열, 사각형에 같은 숫자가 존재하는지 체크
                if is_exist(nr, nc, n2):
                    continue

                # 도미노 중복 체크
                if domino[(min(n1, n2), max(n1, n2))]:
                    continue

                # 판, 사용한 도미노, (행별, 열별, 사각형별 존재하는 숫자) 체크
                board[r][c], board[nr][nc] = n1, n2
                # print(r, c)
                # for b in board:
                #     print(b)
                # return 1
                domino[(min(n1, n2), max(n1, n2))] = 1
                visit(r, c, n1, 1)
                visit(nr, nc, n2, 1)

                # 다음 위치 탐색
                if fill(idx + 1):
                    return 1

                # 초기화
                board[r][c], board[nr][nc] = 0, 0
                domino[(min(n1, n2), max(n1, n2))] = 0
                visit(r, c, n1, 0)
                visit(nr, nc, n2, 0)

    return 0

###########################################################################################################

# 테스트 케이스
TC = 1
while True:
    # 도미노 개수
    N = int(input())

    # 테스트 케이스가 끝난 경우
    if N == 0:
        break

    # 스도미노쿠 판
    board = [[0] * 9 for _ in range(9)]

    # 행별, 열별, 사각형별 존재하는 숫자 체크
    rows = columns = square = 0

    # 사용한 도미노 타일 체크
    domino = defaultdict(int)
    for _ in range(N):
        # 도미노 숫자, 위치
        U, LU, V, LV = map(lambda x: get_pos(x) if len(x) == 2 else int(x), input().split())

        # 판, 사용한 도미노 체크
        board[LU[0]][LU[1]] = U
        board[LV[0]][LV[1]] = V
        domino[(min(U, V), max(U, V))] = 1

        # 행별, 열별, 사각형별 존재하는 숫자 체크
        visit(LU[0], LU[1], U, 1)
        visit(LV[0], LV[1], V, 1)

    # 채워져 있는 숫자 체크
    for i, pos in enumerate(list(input().split()), start = 1):
        r, c = get_pos(pos)
        board[r][c] = i
        visit(r, c, i, 1)

    # 채워져 있지 않은 숫자 위치
    empty = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

    # 모두 채워져 있지 않은 경우, 하나씩 채우기
    if empty:
        fill(0)

    # 판 출력
    print(f'Puzzle {TC}')
    for b in board:
        print(''.join(map(str, b)))
    TC += 1
