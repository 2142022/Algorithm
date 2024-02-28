import sys
input = sys.stdin.readline

# 시계 방향으로 90도 회전
def rotate(b):
    return list(map(list, zip(*b[::-1])))

#########################################################################

# 뒤집기
def change(b):
    return list(map(list, zip(*b)))

#########################################################################

# 회전 3번
def rotate3(b):
    for _ in range(3):
        b = rotate(b)
        blocks.append(b)

#########################################################################

# 블럭 안에 적힌 숫자합 구하기
def get_sum():
    # 숫자합
    s = 0
    for r in range(R):
        for c in range(C):
            if b[r][c]:
                s += board[i + r][j + c]

    return s

#########################################################################

# 이차원 영역 크기
n, m = map(int, input().split())

# 이차원 영역
board = [list(map(int, input().split())) for _ in range(n)]

# 모든 블럭
blocks = []

# 블럭1를 회전하거나 뒤집었을 때의 모든 모양
b1 = [[1, 1, 1, 1]]
blocks.append(b1)
blocks.append(rotate(b1))

# 블럭2를 회전하거나 뒤집었을 때의 모든 모양
b2 = [[1, 1], [1, 1]]
blocks.append(b2)

# 블럭3를 회전하거나 뒤집었을 때의 모든 모양
b3 = [[1, 0], [1, 0], [1, 1]]
blocks.append(b3)
rotate3(b3)
b3 = change(b3)
blocks.append(b3)
rotate3(b3)

# 블럭4를 회전하거나 뒤집었을 때의 모든 모양
b4 = [[1, 0], [1, 1], [0, 1]]
blocks.append(b4)
blocks.append(rotate(b4))
b4 = change(b4)
blocks.append(b4)
blocks.append(rotate(b4))

# 블럭5를 회전하거나 뒤집었을 때의 모든 모양
b5 = [[1, 0], [1, 1], [1, 0]]
blocks.append(b5)
rotate3(b5)

# 블럭 안에 적힌 숫자합의 최대값
max_s = 0

# 블럭
for b in blocks:
    # 블럭 크기
    R, C = len(b), len(b[0])

    # 블럭 시작 위치
    for i in range(n - R + 1):
        for j in range(m - C + 1):
            # 블럭 안에 적힌 숫자합의 최대값
            max_s = max(max_s, get_sum())

print(max_s)
