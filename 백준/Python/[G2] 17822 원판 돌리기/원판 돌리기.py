import sys
input = sys.stdin.readline

# 원판 개수, 하나의 원판에 있는 숫자 수, 회전 수
N, M, T = map(int, input().split())

# 원판에 적힌 수
board = [list(map(int, input().split())) for _ in range(N)]

# 회전하기
for _ in range(T):
    # 회전시킬 원판 번호, 회전 방향, 회전 칸 수
    X, D, K = map(int, input().split())
    for x in range(X, N + 1, X):
        if D == 0:
            board[x - 1] = board[x - 1][M - K:] + board[x - 1][:M - K]
        else:
            board[x - 1] = board[x - 1][K:] + board[x - 1][:K]

    # 원판의 모든 숫자의 합
    total = 0
    # 숫자의 개수
    cnt = 0

    # 인접한 수 지우기
    remove = set()
    for i in range(N):
        for j in range(M):
            num = board[i][j]
            if num:
                total += num
                cnt += 1
                for r, c in ((i + 1, j), (i, (j + 1) % M)):
                    if r >= N:
                        continue
                    if board[r][c] == num:
                        remove.add((r, c))
                        remove.add((i, j))

    # 지우기
    if remove:
        for r, c in remove:
            board[r][c] = 0

    # 지울 수가 없는 경우
    elif cnt:
        mean = total / cnt
        for i in range(N):
            for j in range(M):
                if board[i][j] > mean:
                    board[i][j] -= 1
                elif 0 < board[i][j] < mean:
                    board[i][j] += 1

# 원판에 적힌 수의 합
res = 0
for b in board:
    res += sum(b)

print(res)