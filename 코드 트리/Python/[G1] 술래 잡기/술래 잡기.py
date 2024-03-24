from collections import deque
import sys
input = sys.stdin.readline

# 술래와 거리가 3이하인 도망자 위치, 방향, 수 찾기
# (sr, sc): 현재 술래 위치
def who(sr, sc):
    # 술래 위치에 도망자가 있는 경우 추가
    # 나무에 가려져서 안 잡혔을 수도 있기 때문에 확인
    for i in range(4):
        if board[sr][sc][i]:
            pos.append((sr, sc, i, board[sr][sc][i]))

    # 방문 체크 (이동 거리 저장)
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    # 탐색 위치를 담은 큐
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        t = visited[r][c]

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue
            visited[nr][nc] = t + 1

            # 도망자가 있는 경우 추가
            for i in range(4):
                if board[nr][nc][i]:
                    pos.append((nr, nc, i, board[nr][nc][i]))

            # 거리가 3 미만인 경우 큐에 추가
            # 시작 지점을 1로 했기 때문에 4와 비교
            if t + 1 < 4:
                q.append((nr, nc))

#############################################################################

# 도망자 이동
def run():
    # 도망자 위치, 방향, 수
    for r, c, d, t in pos:
        # 다음 위치, 방향
        nr, nc = r + dr[d], c + dc[d]
        nd = d

        # 범위를 벗어나는 경우, 반대 방향으로 바꾸기
        if not (0 <= nr < N and 0 <= nc < N):
            nd = (nd + 2) % 4
            nr, nc = r + dr[nd], c + dc[nd]

        # 다음 위치에 술래가 없는 경우 이동
        if (nr, nc) != (pr, pc):
            board[nr][nc][nd] += t
            board[r][c][d] -= t

#############################################################################

# 도망자 찾기
# (r, c, d): 현재 술래 위치, 방향
def find(r, c, d):
    # 술래가 잡은 도망자 수
    cnt = 0

    # 현재 칸 포함 3칸 확인
    for i in range(3):
        # 탐색 칸
        nr, nc = r + dr[d] * i, c + dc[d] * i

        # 범위를 벗어나는 경우 끝
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        # 나무가 있는 경우 패스
        if board[nr][nc][4]:
            continue

        # 도망자 확인
        for j in range(4):
            if board[nr][nc][j]:
                cnt += board[nr][nc][j]
                board[nr][nc][j] = 0

    return cnt

#############################################################################

# 격자 크기, 도망자 수, 나무 수, 턴 수
N, M, H, K = map(int, input().split())

# 각 칸에 있는 도망자 수와 나무 존재 여부 체크 (도망자: 0 ~ 3, 나무: 4)
board = [[[0] * 5 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c][d] += 1
for _ in range(H):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c][4] += 1

# 술래 위치, 이동 방향, 회전 방향
pr = pc = N // 2
pd = 0
right = 1

# 총 점수
score = 0

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# K턴 진행
for k in range(1, K + 1):
    # 술래와 거리가 3이하인 도망자 위치, 방향
    pos = []
    who(pr, pc)

    # 도망자 이동
    run()

    # 술래 이동
    pr += dr[pd]
    pc += dc[pd]

    # 방향 전환
    if pr == pc == 0 or pr == pc == N // 2:
        right *= -1
        pd = (pd + 2) % 4
    elif pr + pc == N - 1 or (pr < N // 2 and pc == pr + 1) or (pr > N // 2 and pr == pc):
        pd = (pd + right) % 4

    # 도망자 찾기
    cnt = find(pr, pc, pd)
    score += k * cnt

print(score)