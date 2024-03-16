from collections import defaultdict
import sys
input = sys.stdin.readline

# 모든 블럭 위로 이동
def up():
    # 바꾼 수의 개수
    change = []

    # 열
    for c in range(N):
        # 블럭을 이동시킬 행
        i = 0

        # 행
        for r in range(N):
            # 현재 블럭
            num = board[r][c]
            if num:
                # 마지막 행인 경우 이동만 하기
                if r == N - 1:
                    if i != r:
                        board[i][c] = num
                        board[r][c] = 0
                    break

                # 다음 블럭 찾기
                nr = r + 1
                while nr < N and board[nr][c] == 0:
                    nr += 1
                if nr < N and board[nr][c]:
                    # 같은 수인 경우 합치기
                    if board[nr][c] == num:
                        T[num] -= 2
                        T[num * 2] += 1
                        board[i][c] = num * 2
                        if i != r:
                            board[r][c] = 0
                        board[nr][c] = 0
                        i += 1
                        change.append((num, 2))
                        change.append((num * 2, -1))

                    # 다른 수인 경우 현재 블럭 이동만 하기
                    elif i != r:
                        board[i][c] = num
                        board[r][c] = 0
                        i += 1
                    else:
                        i += 1
                elif i != r:
                    board[i][c] = num
                    board[r][c] = 0
                    i += 1

    return change

################################################################################

# 블록 이동하기
# cnt: 블록 이동 횟수
def move(cnt):
    global max_num, board

    # 5번 이동했으면 끝내기
    if cnt == 5:
        max_num = max(max_num, sorted([k for k, v in T.items() if v])[-1])
        if max_num == total:
            return 1
        return 0

    # 더 이상 합칠 수 있는 숫자가 없으면 끝내기
    if not [v for v in T.values() if v > 1]:
        max_num = max(max_num, sorted([k for k, v in T.items() if v])[-1])
        if max_num == total:
            return 1
        return 0

    board_copy = [b[:] for b in board]

    # 블록 이동 방향
    for d in range(4):
        # 위로 이동
        if d == 0:
            change = up()

        # 아래로 이동
        elif d == 1:
            for _ in range(2):
                board = list(map(list, zip(*board[::-1])))
            change = up()
            for _ in range(2):
                board = list(map(list, zip(*board[::-1])))

        # 왼쪽으로 이동
        elif d == 2:
            board = list(map(list, zip(*board[::-1])))
            change = up()
            board = list(map(list, zip(*board)))[::-1]

        # 오른쪽으로 이동
        else:
            board = list(map(list, zip(*board)))[::-1]
            change = up()
            board = list(map(list, zip(*board[::-1])))

        # 다음 이동
        if move(cnt + 1):
            return 1

        # 초기화
        board = [b[:] for b in board_copy]
        for i, j in change:
            T[i] += j

################################################################################

# 보드 크기
N = int(input())

# 보드
board = []

# 2의 제곱수 개수
T = defaultdict(int)

# 가장 큰 블록
max_num = 0

# 모든 블럭의 합
total = 0
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for info in row:
        if info:
            T[info] += 1
            max_num = max(max_num, info)
            total += info

# 블록 이동하기
move(0)

print(max_num)