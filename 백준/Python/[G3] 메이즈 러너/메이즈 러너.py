import sys
input = sys.stdin.readline

# (sr, sc)에서 이동할 위치 구하기
def find_next(sr, sc):
    # 기존 거리
    origin = abs(sr - er) + abs(sc - ec)

    # 사방 탐색
    for d in range(4):
        nr, nc = sr + dr[d], sc + dc[d]

        # 범위 체크
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        # 벽 체크
        if board[nr][nc] < 0:
            continue

        # 출구와 가까워지는 경우
        if abs(nr - er) + abs(nc - ec) < origin:
            return nr, nc

    # 이동이 불가능한 경우
    return sr, sc

############################################################################

# 참가자 이동
def move():
    global dist, finish, board

    # 사람들의 새로운 위치
    after = [b[:] for b in board]

    # 한 사람씩 이동
    for r in range(N):
        for c in range(N):
            cnt = board[r][c]
            if 0 < cnt <= 10:
                # 이동할 위치
                nr, nc = find_next(r, c)

                # 탈출한 경우
                if (nr, nc) == (er, ec):
                    dist += cnt
                    finish += cnt
                    after[r][c] -= cnt
                    continue

                # 이동
                if (nr, nc) != (r, c):
                    after[nr][nc] += cnt
                    after[r][c] -= cnt
                    dist += cnt

    board = after

############################################################################

# 회전 범위 구하기
def get_bound():
    # 정사각형 한 변의 길이
    for l in range(2, N + 1):
        # 정사각형 시작 지점
        for br in range(N - l + 1):
            for bc in range(N - l + 1):
                # 출구가 없으면 패스
                if not (br <= er < br + l and bc <= ec < bc + l):
                    continue

                # 사람이 있는 경우 끝내기
                for r in range(br, br + l):
                    for c in range(bc, bc + l):
                        if 0 < board[r][c] <= 10:
                            return br, bc, br + l - 1, bc + l - 1

############################################################################

# 회전
def rotate():
    global er, ec

    # 회전 범위 구하기
    br1, bc1, br2, bc2 = get_bound()

    # 격자 회전
    after = list(map(list, zip(*[b[bc1:bc2 + 1] for b in board[br1:br2 + 1]][::-1])))
    for i in range(br2 - br1 + 1):
        board[i + br1][bc1:bc2 + 1] = after[i]

    # 출구 찾기 & 벽은 내구도 -1
    for r in range(br1, br2 + 1):
        for c in range(bc1, bc2 + 1):
            num = board[r][c]
            # 출구 이동
            if num == 100:
                er, ec = r, c

            # 벽 내구도 감소
            elif num < 0:
                board[r][c] += 1

############################################################################

# 미로 크기, 참가자 수, 라운드 수
N, M, K = map(int, input().split())

# 미로 (0: 빈 칸, -1 ~ -9: 벽 내구도, 1 ~ 10: 사람 수, 100: 출구)
board = [list(map(lambda x: -int(x), input().split())) for _ in range(N)]

# 사람 체크
for _ in range(M):
    r, c = map(lambda x: int(x) - 1, input().split())
    board[r][c] += 1

# 출구 좌표
er, ec = map(lambda x: int(x) - 1, input().split())
board[er][ec] = 100

# 사방 탐색용 (상하좌우)
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 이동 거리 합
dist = 0

# 탈출한 사람 수
finish = 0

# K 라운드 진행
for R in range(K):
    # 참가자 이동
    move()

    # 모든 사람이 탈출한 경우 끝내기
    if finish == M:
        break

    # 회전
    rotate()

# 이동 거리 합, 출구 좌표
print(dist)
print(er + 1, ec + 1)