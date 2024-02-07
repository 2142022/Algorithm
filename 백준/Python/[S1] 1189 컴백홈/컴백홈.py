import sys
input = sys.stdin.readline

# 한 칸씩 이동
# (r, c): 현재 위치
def dfs(r, c):
    global cnt

    # 현재까지의 이동 거리
    l = board[r][c]

    # K보다 큰 경우 끝내기
    if l > K:
        return

    # 도착한 경우
    if r == 0 and c == C - 1:
        if l == K:
            cnt += 1
        return

    # 사방 탐색
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 0:
            board[nr][nc] = l + 1
            dfs(nr, nc)
            board[nr][nc] = 0

############################################################################

# 맵 크기, 이동 거리
R, C, K = map(int, input().split())

# 맵
board = [list(map(lambda x: 0 if x == '.' else -1, input().rstrip())) for _ in range(R)]
board[R - 1][0] = 1

# 거리가 K인 가짓수
cnt = 0

# 한 칸씩 이동
dfs(R - 1, 0)

print(cnt)