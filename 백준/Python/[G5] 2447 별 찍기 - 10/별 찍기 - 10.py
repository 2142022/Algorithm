import sys
input = sys.stdin.readline

# 재귀로 중간 뚫기
# (r, c): 패턴 시작점
# n: 패턴 크기
def dfs(r, c, n):
    # 더 이상 패턴을 만들 수 없는 경우 끝내기
    if n == 1:
        return

    # 가운데 별 뚫기
    l = n // 3
    for i in range(r + l, r + 2 * l):
        for j in range(c + l, c + 2 * l):
            board[i][j] = ' '

    # 8방의 작은 패턴 탐색
    for nr, nc in ((r, c), (r, c + l), (r, c + 2 * l), (r + l, c), (r + l, c + l), (r + l, c + 2 * l), (r + 2 * l, c), (r + 2 * l, c + l), (r + 2 * l, c + 2 * l)):
        dfs(nr, nc, l)

###########################################################################################################################################################################

# 패턴 크기
N = int(input())

# 패턴
board = [['*'] * N for _ in range(N)]

# 재귀로 중간 뚫기
dfs(0, 0, N)

# 출력
for i in board:
    print(''.join(i))