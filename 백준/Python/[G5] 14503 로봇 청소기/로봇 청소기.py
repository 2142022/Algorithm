import sys
input = sys.stdin.readline

# 방의 크기
N, M = map(int, input().split())

# 청소기의 위치, 방향
r, c, d = map(int, input().split())

# 방의 청소 상태
clean = [list(map(int, input().split())) for _ in range(N)]

# 상우하좌 탐색
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 청소 완료 체크
unfinished = [[[0] * 4 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        for k in range(4):
            if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and not clean[i + dr[k]][j + dc[k]]:
                unfinished[i][j][k] = 1

# 청소하는 칸의 개수
cnt = 0

# 청소하기
while True:
    # 아직 청소되지 않는 칸인 경우
    if not clean[r][c]:
        # 청소하기
        clean[r][c] = 2
        cnt += 1

        # 청소 완료 체크
        for i in range(4):
            if 0 <= r + dr[i] < N and 0 <= c + dc[i] < M:
                unfinished[r + dr[i]][c + dc[i]][(i + 2) % 4] = 0

    # 사방에 청소되지 않은 칸이 있는 경우
    if unfinished[r][c][0] or unfinished[r][c][1] or unfinished[r][c][2] or unfinished[r][c][3]:
        # 이동 방향에 청소되지 않은 칸이 있을 때까지 회전
        while True:
            d = (d - 1) % 4
            if unfinished[r][c][d]:
                r += dr[d]
                c += dc[d]
                break

    # 사방이 모두 청소된 경우
    else:
        # 후진
        bd = (d + 2) % 4
        r += dr[bd]
        c += dc[bd]

        # 후진했을 때 벽이 있다면 끝내기
        if clean[r][c] == 1:
            break

print(cnt)