from collections import deque
import sys
input = sys.stdin.readline

# 폭탄 시간은 -1하고 빈 곳에 폭탄 생성
def add():
    global R, C

    for i in range(R):
        for j in range(C):
            # 폭탄의 시간 -1
            if board[i][j] > 0:
                board[i][j] -= 1

            # 빈 곳은 폭탄 생성
            else:
                board[i][j] = 3

# 폭탄 시간은 -1하고, 폭탄은 폭발
def burst():
    global R, C

    # 폭발할 폭탄이 있는 위치
    queue = deque()

    for i in range(R):
        for j in range(C):
            # 폭발할 폭탄이 아닌 폭탄의 시간 -1
            if board[i][j] > 1:
                board[i][j] -= 1

            # 폭발할 폭탄은 큐에 올리기
            if board[i][j] == 1:
                queue.append([i, j])
                board[i][j] = 0
            

    # 큐에 원소가 없어질 때까지 반복
    while queue:
        i, j = queue.popleft()

        # 폭탄의 사방 폭발
        if i - 1 >= 0:
            board[i - 1][j] = 0
        if i + 1 < R:
            board[i + 1][j] = 0
        if j - 1 >= 0:
            board[i][j - 1] = 0
        if j + 1 < C:
            board[i][j + 1] = 0
                

# R X C 격자판, N초 후의 격자판 상태 구하기
R, C, N = map(int, input().split())

# 초기 격자 상태: 폭탄이 몇 초 뒤에 터지는지 입력받기
board = [[0] * C for i in range(R)]

for i in range(R):
    tmp = list(input().strip())

    for j in range(C):
        if tmp[j] == '.':
            board[i][j] = 0
        else:
            # 원래는 3으로 입력받아야 하지만 어차피 1초 후의 상태는 2
            board[i][j] = 2

# N초 후의 격자판 상태 구하기
# 1초 후에는 초기 상태와 똑같으므로 제외
for i in range(2, N+1):
    # 짝수 초에는 폭탄 시간 -1, 빈 곳에 폭탄 생성
    if i % 2 == 0:
        add()

    # 홀수 초에는 폭탄 시간 -1, 폭탄 폭발
    else:
        burst()

# 출력
for i in range(R):
    for j in range(C):
        if board[i][j] == 0:
            print('.', end = '')
        else:
            print('O', end = '')
    print()
