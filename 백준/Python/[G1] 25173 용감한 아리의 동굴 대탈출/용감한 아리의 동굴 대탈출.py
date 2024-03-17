from collections import deque
import sys
input = sys.stdin.readline

# 보스가 소환할 몬스터 위치 찾기
# (r, c): 탐색 위치
# d: 탐색 진행 방향
def find_monster(r, c, d):
    # 이동할 칸 수
    cnt = 1

    while True:
        # 두 번씩 이동
        for _ in range(2):
            for _ in range(cnt):
                r += dr[d]
                c += dc[d]

                # 석순이 있는 경우 끝
                if 0 <= r < N and 0 <= c < M and board[r][c]:
                    return r, c

            # 회전
            d = (d + 1) % 4

        cnt += 1

############################################################################################################

# 현재 소환된 몬스터가 아리를 공격할 때의 공격력 구하기
def attack(mr, mc):
    # 아리에게 가기 전 소멸하는 경우
    if abs(mr - ar) + abs(mc - ac) >= E:
        return 0

    # 방문 체크
    visited = [[0] * M for _ in range(N)]
    visited[mr][mc] = 1

    # 탐색 위치, 그 때의 공격력을 담은 큐
    q = deque([(mr, mc, E)])
    while q:
        r, c, t = q.popleft()

        # 더 이상 이동해도 공격력이 0이 되는 경우 끝내기
        if t - 1 == 0:
            return 0

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 아리가 있는 경우 끝내기
            if (nr, nc) == (ar, ac):
                return t - 1

            # 범위, 보스, 석순 체크
            if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] or (nr, nc) == (br, bc):
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1

            # 이동
            q.append((nr, nc, t - 1))

    # 아리에게까지 못 가는 경우
    return 0

############################################################################################################

# 아리의 승리 여부 구하기
def play():
    global ar, ac, ad, br, bc, bd, A, B

    # 아리의 이동 전 마지막 위치
    par, pac = ar, ac

    # 아리, 보스 중 한 명이라도 체력이 0 이하가 되면 끝
    while True:
        # 아리 공격
        B -= D

        # 보스 소멸
        if B <= 0:
            return "VICTORY!"

        # 아리 이동 (최대 4번 회전 가능)
        for _ in range(4):
            nar, nac = ar + dr[ad], ac + dc[ad]

            # 범위, 석순, 보스 체크
            if not (0 <= nar < N and 0 <= nac < M) or board[nar][nac] or (nar, nac) == (br, bc):
                ad = (ad + 1) % 4
                A -= 1
                if A <= 0:
                    return "CAVELIFE..."
            else:
                par, pac = ar, ac
                ar, ac = nar, nac
                break

        # 보스가 소환할 몬스터 위치 찾기
        mr = mc = -1
        if len(pos) == 1:
            mr, mc = pos[0]
        elif len(pos) > 1:
            mr, mc = find_monster(br, bc, bd)

        # 현재 소환된 몬스터가 아리 위치까지 이동할 수 있는 경우 공격
        if mr != -1:
            A -= attack(mr, mc)
            if A <= 0:
                return "CAVELIFE..."

        # 아리가 이동을 했다면 보스 이동
        if (par, pac) != (ar, ac):
            br, bc, bd = par, pac, ad

############################################################################################################

# 동굴 크기
N, M = map(int, input().split())

# 동굴 상태
board = []

# 아리, 보스 위치
ar = ac = br = bc = -1

# 석순 위치
pos = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j, info in enumerate(row):
        if info == 1:
            pos.append((i, j))
        elif info == 2:
            ar, ac = i, j
            board[i][j] = 0
        elif info == 3:
            br, bc = i, j
            board[i][j] = 0

# 아리, 보스의 진행 방향
ad = bd = 0
if ac - bc == 1:
    ad = bd = 1
elif ar - br == 1:
    ad = bd = 2
elif ac - bc == -1:
    ad = bd = 3

# 아리 체력, 공격력, 보스 체력, 공격력
A, D, B, E = map(int, input().split())

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 아리의 승리 여부 구하기
print(play())