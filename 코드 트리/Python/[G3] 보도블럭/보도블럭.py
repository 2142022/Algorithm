import sys
input = sys.stdin.readline

# i행을 지나갈 수 있는지 확인
def possible(i):
    # 경사로를 설치한 열 체크
    visited = [0] * n

    # 높이를 내림차순으로 저장한 스택
    stack = []

    # 왼쪽에서 오른쪽으로 탐색
    for j in range(n):
        if stack and board[i][j] > board[i][stack[-1]]:
            if board[i][j] - board[i][stack[-1]] > 1:
                return 0
            h = board[i][stack[-1]]
            l = 0
            while stack and board[i][stack[-1]] == h and l < L:
                visited[stack.pop()] = 1
                l += 1
            if l != L:
                return 0
            stack = []
        stack.append(j)

    # 오른쪽에서 왼쪽으로 탐색
    for j in range(n - 1, -1, -1):
        if stack and board[i][j] > board[i][stack[-1]]:
            if board[i][j] - board[i][stack[-1]] > 1:
                return 0
            h = board[i][stack[-1]]
            l = 0
            while stack and board[i][stack[-1]] == h and l < L:
                idx = stack.pop()
                if visited[idx]:
                    return 0
                visited[idx] = 1
                l += 1
            if l != L:
                return 0
            stack = []
        stack.append(j)

    # 현재 행을 지나갈 수 있는 경우
    return 1

##########################################################################

# 지나갈 수 있는 행과 열의 개수 구하기
def get_cnt():
    global cnt

    # 행
    for i in range(n):
        # 현재 행을 지나갈 수 있는지 확인
        if possible(i):
            cnt += 1

##########################################################################

# 보도블럭 크기, 경사로 길이
n, L = map(int, input().split())

# 보도블럭 높이
board = [list(map(int, input().split())) for _ in range(n)]

# 지나갈 수 있는 행과 열의 개수
cnt = 0
get_cnt()
# 보도 블럭 회전
board = list(map(list, zip(*board[::-1])))
get_cnt()

print(cnt)