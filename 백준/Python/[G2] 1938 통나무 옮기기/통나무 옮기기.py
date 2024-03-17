from collections import deque
import sys
input = sys.stdin.readline

# 통나무 최소 동작 횟수 구하기
def move():
    # 위치, 방향별 최소 동작 횟수
    cnt = [[[N * N] * N for _ in range(N)] for _ in range(2)]
    cnt[sd][sr][sc] = 0

    # 탐색 위치와 방향을 담은 큐
    q = deque([(sr, sc, sd)])
    while q:
        r, c, d = q.popleft()

        # 현재까지의 최소 동작 횟수
        t = cnt[d][r][c]

        # 도착지점인 경우 끝내기
        if (r, c, d) == (er, ec, ed):
            return t

        # 현재 통나무가 가로로 있는 경우
        if d == 0:
            # 상
            if r - 1 >= 0 and cnt[d][r - 1][c] > t + 1 and sum(board[r - 1][c - 1:c + 2]) == 0:
                cnt[d][r - 1][c] = t + 1
                q.append((r - 1, c, d))
            # 하
            if r + 1 < N and cnt[d][r + 1][c] > t + 1 and sum(board[r + 1][c - 1:c + 2]) == 0:
                cnt[d][r + 1][c] = t + 1
                q.append((r + 1, c, d))
            # 좌
            if c - 2 >= 0 and cnt[d][r][c - 1] > t + 1 and board[r][c - 2] == 0:
                cnt[d][r][c - 1] = t + 1
                q.append((r, c - 1, d))
            # 우
            if c + 2 < N and cnt[d][r][c + 1] > t + 1 and board[r][c + 2] == 0:
                cnt[d][r][c + 1] = t + 1
                q.append((r, c + 1, d))
            # 회전
            if 1 <= r < N - 1 and cnt[1][r][c] > t + 1 and sum(board[r - 1][c - 1:c + 2]) == sum(board[r + 1][c - 1:c + 2]) == 0:
                cnt[1][r][c] = t + 1
                q.append((r, c, 1))

        # 현재 통나무가 세로로 있는 경우
        else:
            # 상
            if r - 2 >= 0 and cnt[d][r - 1][c] > t + 1 and board[r - 2][c] == 0:
                cnt[d][r - 1][c] = t + 1
                q.append((r - 1, c, d))
            # 하
            if r + 2 < N and cnt[d][r + 1][c] > t + 1 and board[r + 2][c] == 0:
                cnt[d][r + 1][c] = t + 1
                q.append((r + 1, c, d))
            # 좌
            if c - 1 >= 0 and cnt[d][r][c - 1] > t + 1 and board[r - 1][c - 1] == board[r][c - 1] == board[r + 1][c - 1] == 0:
                cnt[d][r][c - 1] = t + 1
                q.append((r, c - 1, d))
            # 우
            if c + 1 < N and cnt[d][r][c + 1] > t + 1 and board[r - 1][c + 1] == board[r][c + 1] == board[r + 1][c + 1] == 0:
                cnt[d][r][c + 1] = t + 1
                q.append((r, c + 1, d))
            # 회전
            if 1 <= c < N - 1 and cnt[0][r][c] > t + 1 and board[r - 1][c - 1] == board[r][c - 1] == board[r + 1][c - 1] == board[r - 1][c + 1] == board[r][c + 1] == board[r + 1][c + 1] == 0:
                cnt[0][r][c] = t + 1
                q.append((r, c, 0))

    # 도착이 불가능한 경우
    return 0

#############################################################################################################################################################################################################

# 평지 크기
N = int(input())

# 지형 정보
board = []

# 통나무 시작 위치
B = []

# 통나무 도착 위치
E = []

# 입력 받기
for i in range(N):
    row = list(map(lambda x: {'0': 0, '1': 1, 'B': 2, 'E': 3}[x], input().rstrip()))
    board.append(row)
    for j, info in enumerate(row):
        if info == 2:
            B.append((i, j))
            board[i][j] = 0
        elif info == 3:
            E.append((i, j))
            board[i][j] = 0

# 중간 통나무의 시작과 도착의 위치, 방향
sr = sc = sd = er = ec = ed = -1
if B[0][0] == B[1][0]:
    sr, sc, sd = *B[1], 0
else:
    sr, sc, sd = *B[1], 1
if E[0][0] == E[1][0]:
    er, ec, ed = *E[1], 0
else:
    er, ec, ed = *E[1], 1

# 통나무 최소 동작 횟수
print(move())