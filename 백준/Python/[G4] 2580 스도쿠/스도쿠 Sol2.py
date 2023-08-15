import sys
input = sys.stdin.readline

# 같은 행과 같은 열 체크하기
# r: 현재 행
# c: 현재 열
# num: 확인하려는 숫자
def check1(r, c, num):
    for i in range(9):
        if sudoku[r][i] == num or sudoku[i][c] == num:
            return False
    return True

#############################################################################

# 같은 부분 사각형 체크하기
# r: 부분 사각형의 시작 행
# c: 부분 사각형의 시작 열
# num: 확인하려는 숫자
def check2(r, c, num):
    for i in range(3):
        for j in range(3):
            if sudoku[r + i][c + j] == num:
                return False
    return True

#############################################################################

# DFS로 한 칸씩 채우기
# idx: 빈 칸의 인덱스
def dfs(idx):
    # 모든 칸을 다 채운 경우 출력 후 끝내기
    if idx == len(empty):
        for i in range(9):
            print(*sudoku[i])
        exit()

    # 현재 위치
    r, c = empty[idx]

    # 부분 사각형에서의 행과 열
    sr = r // 3 * 3
    sc = c // 3 * 3

    for num in range(1, 10):
        # 같은 행, 같은 열, 같은 부분 사각형에 있는 수 제외
        if check1(r, c, num) and check2(sr, sc, num):
            sudoku[r][c] = num
            dfs(idx + 1)
            sudoku[r][c] = 0


#############################################################################

# 스도쿠 입력받기
sudoku = [list(map(int, input().split())) for _ in range(9)]

# 빈 칸 위치 정보
empty = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append((i, j))

# DFS로 빈 칸 채우기
dfs(0)
