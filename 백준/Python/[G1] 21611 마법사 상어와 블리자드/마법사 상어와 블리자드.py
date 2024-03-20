from collections import defaultdict
import sys
input = sys.stdin.readline

# 각 칸의 구슬 정보를 1차 리스트로 바꾸기
def get_board():
    global board

    # 시작 위치, 방향
    r, c = sr, sc
    d = 3

    # 한 변에서의 이동 횟수
    i = 1
    cnt = 1
    while cnt < N:
        # 2번 저장
        for _ in range(2):
            for _ in range(cnt):
                r += dr[d]
                c += dc[d]
                board.append(info[r][c])
                idx[(r, c)] = i
                i += 1

            # 회전
            d = (d - 1) % 4
        cnt += 1

    # 마지막 N - 1개의 구슬 더하기
    for j in range(N - 2, -1, -1):
        board.append(info[0][j])
        idx[(0, j)] = i
        i += 1

###############################################################################

# 파괴 (d방향으로 s개 파괴) & 이동
def destroy(s, d):
    global board

    # 파괴할 칸
    r, c = sr + dr[d], sc + dc[d]
    for _ in range(s):
        i = idx[(r, c)]
        board[i] = 0
        r += dr[d]
        c += dc[d]

    # 이동
    board = [0] + [b for b in board if b]
    board += [0] * (N * N - len(board))

###############################################################################

# 연속하는 4개의 구슬 폭발 & 이동
def explode():
    global board

    # 폭발할 구슬의 위치
    pos = set()

    # 인덱스
    i = 1
    while i < N * N:
        # 현재 구슬 번호
        num = board[i]

        # 0이 나오면 끝
        if not num:
            break

        # 연속되는 구슬 개수
        same = 1
        while i + same < N * N and board[i + same] == num:
            same += 1

        # 4개 이상이면 폭발
        if same >= 4:
            for j in range(i, i + same):
                pos.add(j)
            cnt[num] += same

        # 다음 탐색 위치
        i += same

    # 폭발 & 이동
    board = [0] + [b for i, b in enumerate(board) if b and i not in pos]
    board += [0] * (N * N - len(board))

    # 폭발 여부 반환
    if pos:
        return 1
    else:
        return 0

###############################################################################

# 변화
def change():
    global board

    # 새로운 구슬 보드
    new = [0]

    # 인덱스
    i = 1
    while i < N * N:
        # 현재 구슬 번호
        num = board[i]

        # 0이 나오면 끝
        if not num:
            break

        # 연속되는 구슬 개수
        same = 1
        while i + same < N * N and board[i + same] == num:
            same += 1

        # 구슬 개수와 번호 저장 (단, 원래 크기까지)
        if len(new) < N * N:
            new.append(same)
        if len(new) < N * N:
            new.append(num)

        # 다음 탐색 위치
        i += same

    # 저장 후 빈 칸 0으로 채우기
    board = new
    board += [0] * (N * N - len(board))

###############################################################################

# 크기, 블리자드 시전 횟수
N, M = map(int, input().split())

# 각 칸의 구슬 정보
info = [list(map(int, input().split())) for _ in range(N)]

# 상어 위치
sr = sc = N // 2

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 각 칸의 인덱스
idx = defaultdict(int)
idx[(sr, sc)] = 0

# 1차 리스트로 바꾸기
board = [0]
get_board()

# 각 구슬의 폭발 횟수
cnt = defaultdict(int)

# M번의 블리자드 시전
for _ in range(M):
    # 방향, 거리
    d, s = map(int, input().split())
    d = {1: 0, 2: 2, 3: 3, 4: 1}[d]

    # 파괴 & 이동
    destroy(s, d)

    # 폭발하는 구슬이 없을 때까지 폭발 & 이동
    while True:
        if not explode():
            break

    # 변화
    change()

# 결과 계산
result = 0
for k, v in cnt.items():
    result += k * v
print(result)