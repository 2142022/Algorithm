from collections import deque
import sys
input = sys.stdin.readline

# 구슬들이 더 이상 움직일 수 있는지 확인
def check(rr, rc, br, bc, dr, dc, rf, bf):
    if rf == 0:
        # 다음 위치가 벽인 경우
        if board[rr + dr][rc + dc] == '#':
            rf = 1
        # 다다음 위치가 벽이면서 다음 위치에 파란 구슬이 있는 경우
        elif board[rr + dr + dr][rc + dc + dc] == '#' and (br, bc) == (rr + dr, rc + dc):
            rf = 1
    # 파란 구슬이 더 이상 움직일 수 없는 경우
    if bf == 0:
        # 다음 위치가 벽인 경우
        if board[br + dr][bc + dc] == '#':
            bf = 1
        # 다다음 위치가 벽이면서 다음 위치에 빨간 구슬이 있는 경우
        elif board[br + dr + dr][bc + dc + dc] == '#' and (rr, rc) == (br + dr, bc + dc):
            bf = 1

    return rf, bf

###################################################################################################

# 구슬들의 다음 위치 및 빨간 구슬 탈출 여부 반환
# (rr, rc): 빨간 구슬의 현재 위치
# (br, bc): 파란 구슬의 현재 위치
# d: 이동 방향 (0: 상, 1: 하, 2: 좌, 3: 우)
def shift(rr, rc, br, bc, d):
    # 움직이는 칸 수
    dr = direction[d][0]
    dc = direction[d][1]

    # 빨간 구슬 탈출 여부
    flag = 0

    # rf: 빨간 구슬이 모두 움직였다면 1, 아직 움직일 수 있다면 0
    # bf: 파란 구슬이 모두 움직였다면 1, 아직 움직일 수 있다면 0
    rf = bf = 0
    rf, bf = check(rr, rc, br, bc, dr, dc, rf, bf)

    while rf == 0 or bf == 0:
        # 구슬들 움직이기
        if rf == 0:
            rr += dr
            rc += dc
        if bf == 0:
            br += dr
            bc += dc

        # 빨간 구슬이 탈출한 경우
        if rf == 0 and board[rr][rc] == 'O':
            flag = 1
            rf = 1
            rr = rc = -1
        # 파란 구슬이 탈출한 경우
        if bf == 0 and board[br][bc] == 'O':
            return -1, -1, -1, -1, -1

        # 구슬들이 더 이상 움직일 수 있는지 확인
        rf, bf = check(rr, rc, br, bc, dr, dc, rf, bf)

    return rr, rc, br, bc, flag

###################################################################################################

# N: 보드의 세로 길이, M: 보드의 가로 길이
N, M = map(int, input().split())

# 빨간 구슬의 처음 위치 (rr, rc)
# 파란 구슬의 처음 위치 (br, bc)
# 구멍의 위치 (hr, hc)
rx = ry = bx = by = hx = hy = -1

# 보드
board = []
for i in range(N):
    # 한 행의 보드 정보
    bi = list(input().rstrip())
    board.append(bi)

    # 구슬과 구멍의 위치 저장
    for j in range(M):
        if bi[j] == 'R':
            rx, ry = i, j
        elif bi[j] == 'B':
            bx, by = i, j
        elif bi[j] == 'O':
            hx, hy = i, j

# 사방 탐색용
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
# 상하좌우를 알파벳으로 표현
alphabet = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}

# 방문 체크용
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# 빨간 구슬의 위치, 파란 구슬의 위치, 현재까지 보드를 기울인 횟수, 기울인 순서를 담은 큐
q = deque()
q.append((rx, ry, bx, by, 0, ''))

# BFS로 빨간 구슬 빼내기
while q:
    # 빨간 구슬의 위치, 파란 구슬의 위치, 현재까지 보드를 기울인 횟수, 기울인 순서
    rr, rc, br, bc, cnt, order = q.popleft()

    # 10번 넘게 기울였다면 끝내기
    if cnt > 10:
        break

    # 사방 탐색
    for i in range(4):
        # 다음 위치 및 빨간 구슬 탈출 여부
        nrr, nrc, nbr, nbc, flag = shift(rr, rc, br, bc, i)

        # 다음 위치로 가는 동안 파란 구슬이 나온 경우, 패스
        if flag == -1:
            continue

        # 다음 위치로 가는 동안 빨간 구슬이 나왔다면 끝내기
        elif flag == 1 and cnt < 10:
            print(cnt + 1)
            print(order + alphabet[i])
            exit()

        # 이미 방문한 곳은 패스
        if visited[nrr][nrc][nbr][nbc]:
            continue

        # 큐에 다음 위치 넣기
        q.append((nrr, nrc, nbr, nbc, cnt + 1, order + alphabet[i]))
        visited[nrr][nrc][nbr][nbc] = 1

# 10번 넘게 기울였거나 큐가 빈 경우 -1 출력
print(-1)