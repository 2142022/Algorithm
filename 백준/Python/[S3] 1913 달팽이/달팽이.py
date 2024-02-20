import sys
input = sys.stdin.readline

# 표 크기
N = int(input())

# 찾는 수
find = int(input())
# 찾는 수의 위치
fr, fc = N // 2, N // 2

# 표
board = [[0] * N for _ in range(N)]

# 시작 지점
r = c = N // 2
board[r][c] = 1
r -= 1

# 채울 수
num = 2

# 채울 사각형의 길이
l = 3
while l <= N:
    # 윗변 채우기
    for i in range(c - l // 2 + 1, c + l // 2 + 1):
        board[r][i] = num
        if num == find:
            fr, fc = r, i
        num += 1

    # 오른쪽 변 채우기
    for i in range(r + 1, r + l):
        board[i][c + l // 2] = num
        if num == find:
            fr, fc = i, c + l // 2
        num += 1

    # 아랫변 채우기
    for i in range(c + l // 2 - 1, c - l // 2 - 1, -1):
        board[r + l - 1][i] = num
        if num == find:
            fr, fc = r + l - 1, i
        num += 1

    # 왼쪽 변 채우기
    for i in range(r + l - 2, r - 1, -1):
        board[i][c - l // 2] = num
        if num == find:
            fr, fc = i, c - l // 2
        num += 1

    l += 2
    r -= 1

for i in board:
    print(*i)
print(fr + 1, fc + 1)