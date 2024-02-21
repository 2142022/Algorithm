import sys
input = sys.stdin.readline

# 인접한 곳에 바다가 3칸이나 4칸이 있는지 확인
def disappear(r, c):
    # 바다 개수
    cnt = 0

    # 사방 탐색
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if not (0 <= nr < R and 0 <= nc < C):
            cnt += 1
            # 3개 이상이 되면 사라질 곳
            if cnt >= 3:
                return 1
            continue

        # 바다 체크
        if board[nr][nc] == '.':
            cnt += 1

        # 3개 이상이 되면 사라질 곳
        if cnt >= 3:
            return 1

    return 0

###############################################################################

# 지도 크기
R, C = map(int, input().split())

# 지도
board = [list(input().rstrip()) for _ in range(R)]

# 50년 후 사라질 땅의 위치
pos = []

# 50년 후의 지도의 경계
rs, re, cs, ce = 10, 0, 10, 0

# 인접한 곳에 바다가 3칸이나 4칸이 있으면 바다로 바꾸기
for i in range(R):
    for j in range(C):
        if board[i][j] == 'X':
            if disappear(i, j):
                pos.append((i, j))
                continue

            # 50년 후에도 땅이 있으면 경계값 비교
            if i < rs:
                rs = i
            if i > re:
                re = i
            if j < cs:
                cs = j
            if j > ce:
                ce = j

# 땅을 바다로 바꾸기
for i, j in pos:
    board[i][j] = '.'

# 50년 후의 지도 출력
for i in range(rs, re + 1):
    print(''.join(board[i][cs:ce + 1]))