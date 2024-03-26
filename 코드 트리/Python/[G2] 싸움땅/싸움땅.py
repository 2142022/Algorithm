from collections import defaultdict
import sys
input = sys.stdin.readline

# 총 획득
def get_gun(x):
    r, c, d, s, g = players[x]

    # 현재 칸에 있는 총들 중 플레이어가 가지고 있는 총보다 공격력이 높은 총
    guns = sorted([k for k in board[r][c] if k > g])
    if guns:
        # 플레이어가 주울 총
        max_g = guns[-1]

        # 현재 총 버리기
        if g:
            board[r][c][g] += 1

        # 총 줍기
        players[x][4] = max_g
        if board[r][c][max_g] == 1:
            board[r][c].pop(max_g)
        else:
            board[r][c][max_g] -= 1

#################################################################################

# 패자 이동
def lose(x):
    r, c, d, s, g = players[x]

    # 총 버리기
    if g:
        players[x][4] = 0
        board[r][c][g] += 1

    # 이동
    for _ in range(4):
        nr, nc = r + dr[d], c + dc[d]

        # 범위를 벗어나거나 다른 플레이어가 있는 경우, 회전
        if not (0 <= nr < N and 0 <= nc < N) or exist[nr][nc] != -1:
            d = (d + 1) % 4
            continue

        # 이동
        r, c = nr, nc
        players[x][:3] = [r, c, d]
        exist[r][c] = x
        break

    # 총 획득
    get_gun(x)


#################################################################################

# 격자 크기, 플레이어 수, 라운드 수
N, M, K = map(int, input().split())

# 총 정보
board = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j, info in enumerate(row):
        if info:
            board[i][j][info] += 1

# 각 칸에 있는 플레이어 번호
exist = [[-1] * N for _ in range(N)]

# 플레이어 위치, 방향, 능력치, 총
players = []
for i in range(M):
    r, c, d, s = list(map(int, input().split()))
    r -= 1
    c -= 1
    players.append([r, c, d, s, 0])
    exist[r][c] = i

# 포인트
points = [0] * M

# 사방 탐색
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 라운드
for _ in range(K):
    # 플레이어 이동
    for i in range(M):
        r, c, d, s, g = players[i]

        # 이동 위치
        nr, nc = r + dr[d], c + dc[d]
        # 범위를 벗어나는 경우, 반대 방향으로 이동
        if not (0 <= nr < N and 0 <= nc < N):
            d = (d + 2) % 4
            nr, nc = r + dr[d], c + dc[d]

        # 이동
        exist[r][c] = -1
        r, c = nr, nc
        players[i][:3] = [r, c, d]

        # 다른 플레이어가 있는지 확인
        j = exist[r][c]

        # 다른 플레이어가 없는 경우, 총 획득
        if j == -1:
            exist[r][c] = i
            get_gun(i)

        # 다른 플레이어가 있는 경우
        else:
            # 다른 플레이어 정보
            tr, tc, td, ts, tg = players[j]

            # 승자 패자 나누기
            if (s + g > ts + tg) or (s + g == ts + tg and s > ts):
                points[i] += s + g - ts - tg

                # 패자 이동
                lose(j)

                # 승자 총 획득
                get_gun(i)
                exist[r][c] = i
            else:
                points[j] += ts + tg - s - g

                # 패자 이동
                lose(i)

                # 승자 총 획득
                get_gun(j)

print(*points)