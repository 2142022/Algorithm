import sys
input = sys.stdin.readline

# 방 크기
N, M = map(int, input().split())

# 로봇 청소기 위치, 방향
r, c, d = map(int, input().split())

# 방 상태
board = [list(map(int, input().split())) for _ in range(N)]

# 사방 탐색용 (상, 우, 하, 좌)
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 방문 체크
visited = [[0] * M for _ in range(N)]
visited[r][c] = 1

# 로봇 청소기가 방문한 칸 수
area = 1

# 로봇 청소기가 움직일 수 없을 때까지 반복
while True:
    # 전진할 수 있을 때까지 4방향 탐색
    for i in range(4):
        # 좌회전
        d = (d - 1) % 4

        # 다음 위치
        nr, nc = r + dr[d], c + dc[d]

        # 전진할 수 있는 경우
        if board[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = 1
            area += 1
            r, c = nr, nc
            break

    # 4방향 모두 갈 수 없는 경우 후진
    else:
        # 후진 위치
        nr, nc = r + dr[(d + 2) % 4], c + dc[(d + 2) % 4]

        # 후진도 불가능한 경우 끝내기
        if board[nr][nc]:
            break

        # 아직 방문하지 않는 경우, 방문 체크
        if not visited[nr][nc]:
            visited[nr][nc] = 1
            area += 1

        # 후진
        r, c = nr, nc

print(area)