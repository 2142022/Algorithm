import sys
input = sys.stdin.readline

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

    # 같은 행, 같은 열, 같은 부분 사각형에 있는 수 제외
    possible = set(range(1, 10)) - set(sudoku[r]) - set(sudoku[i][c] for i in range(9)) \
               - set(sudoku[sr + i][sc + j] for i in range(3) for j in range(3))

    for num in possible:
        sudoku[r][c] = num
        dfs(idx + 1)
        sudoku[r][c] = 0

####################################################################################################

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
