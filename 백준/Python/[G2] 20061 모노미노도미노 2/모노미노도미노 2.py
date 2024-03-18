from collections import defaultdict
import sys
input = sys.stdin.readline

# 블록을 보드로 내리기
# idx: 보드 번호
# t: 블록 모양
# j: 블록의 열
def move(idx, t, j):
    global score

    # 블록이 추가된 행
    row = []

    # 1 X 1
    if t == 1:
        bottom = 4
        for r in range(4, 10):
            if board[idx][r][j]:
                break
            else:
                bottom = r
        board[idx][bottom][j] = 1
        row.append(bottom)

    # 1 X 2
    elif t == 2:
        # 두 블럭 중 놓을 수 있는 가장 작은 행
        bottoms = []
        for c in (j, j + 1):
            bottom = 4
            for r in range(4, 10):
                if board[idx][r][c]:
                    break
                else:
                    bottom = r
            bottoms.append(bottom)
        bottom = min(bottoms)
        board[idx][bottom][j] = board[idx][bottom][j + 1] = 1
        row.append(bottom)

    # 2 X 1
    else:
        bottom = 4
        for r in range(4, 10):
            if board[idx][r][j]:
                break
            else:
                bottom = r
        board[idx][bottom][j] = board[idx][bottom - 1][j] = 1
        row.append(bottom - 1)
        row.append(bottom)

    # 블록이 새로 추가된 행 중 블록이 4개가 된 행
    full = []
    for r in row:
        if sum(board[idx][r]) == 4:
            full.append(r)
            score += 1

    # 꽉찬 행은 지우고 블록 아래로 내리기
    for bottom in full:
        for r in range(bottom, 3, -1):
            board[idx][r] = board[idx][r - 1][:]

##############################################################################

# 보드의 연한 칸에 있는 블록 내리기
# idx: 보드 번호
def down(idx):
    # 연한 칸에 블록이 있는지 확인
    for _ in range(2):
        if sum(board[idx][5]):
            for r in range(9, 3, -1):
                board[idx][r] = board[idx][r - 1][:]

##############################################################################

# 빨강 + 초록, 빨강 + 파랑 (90도 시계방향 회전해서 초록과 동일하게 생각하기)
board = defaultdict(list)
board[0] = [[0] * 4 for _ in range(10)]
board[1] = [[0] * 4 for _ in range(10)]

# 총 점수
score = 0

# 블록 놓기
for _ in range(int(input())):
    # 블록 모양, 블록 위치
    t, r, c = map(int, input().split())

    # 현재 블록 초록색 보드로 내리기
    move(0, t, c)

    # 초록색 보드 연한 칸에 있는 블록 내리기
    down(0)

    # 현재 블록 90도 회전
    if t == 1:
        r, c = c, 3 - r
    elif t == 2:
        r, c = c, 3 - r
        t = 3
    else:
        r, c = c, 2 - r
        t = 2

    # 현재 블록 파란색 보드로 내리기
    move(1, t, c)

    # 파란색 보드 연한 칸에 있는 블록 내리기
    down(1)

# 점수 및 타일이 있는 칸 수 출력
print(score)
cnt = 0
for k in range(2):
    for i in range(10):
        cnt += sum(board[k][i])
print(cnt)
