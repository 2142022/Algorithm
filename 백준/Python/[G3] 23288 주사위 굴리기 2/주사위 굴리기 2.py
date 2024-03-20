from collections import deque
import sys
input = sys.stdin.readline

# 주사위 이동
def move(r, c, d):
    # 이동 위치
    nr, nc = r + dr[d], c + dc[d]

    # 범위 체크 후 이동 방향 변경
    if not (0 <= nr < N and 0 <= nc < M):
        d = (d + 2) % 4
        nr, nc = r + dr[d], c + dc[d]

    # 주사위 전개도 변경
    if d == 0:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    else:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]

    return nr, nc, d

#########################################################################################

# 점수 계산
def get_score(r, c):
    # 현재 위치 번호
    num = board[r][c]

    # 이동할 수 있는 칸 수
    cnt = 1

    # 방문 체크
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1

    # 탐색 위치를 담은 큐
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()

        # 사방 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 범위 및 방문 체크
            if not (0 <= nr < N and 0 <= nc < M) or visited[nr][nc]:
                continue

            # 같은 숫자인 경우
            if board[nr][nc] == num:
                cnt += 1
                visited[nr][nc] = 1
                q.append((nr, nc))

    return cnt * num

##########################################################################

# 지도 크기, 이동 횟수
N, M, K = map(int, input().split())

# 지도
board = [list(map(int, input().split())) for _ in range(N)]

# 주사위
dice = [1, 2, 3, 4, 5, 6]

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 주사위 위치, 방향
r, c, d = 0, 0, 1

# 총 점수
score = 0

# 주사위 이동
for _ in range(K):
    # 주사위 이동
    r, c, d = move(r, c, d)

    # 점수 계산
    score += get_score(r, c)

    # 다음 이동 방향 결정
    if dice[5] > board[r][c]:
        d = (d + 1) % 4
    elif dice[5] < board[r][c]:
        d = (d - 1) % 4

print(score)