from collections import deque
import sys
input = sys.stdin.readline

# 도연이가 만날 수 있는 사람 수 구하기
def get_cnt(r, c):
    # 도연이가 만날 수 있는 사람 수
    cnt = 0

    # 탐색 위치를 담은 큐
    q = deque([(r, c)])
    while q:
        # 탐색 위치
        r, c = q.popleft()

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 사람이 있거나 빈 공간만 돌아다닐 수 있음
            if 0 <= board[nr][nc] <= 1:
                if board[nr][nc] == 1:
                    cnt += 1
                board[nr][nc] = -1
                q.append((nr, nc))

    # 아무도 만나지 못한 경우 TT 반환
    if cnt:
        return cnt
    else:
        return 'TT'

##############################################################################################

# 캠퍼스 크기
N, M = map(int, input().split())

# 캠퍼스
board = []

# 도연이 위치
r = c = -1
for i in range(N):
    row = list(map(lambda x: {'O': 0, 'X': -1, 'I': 100, 'P': 1}[x], input().rstrip()))
    board.append(row)
    if r == -1:
        for j, info in enumerate(row):
            if info == 100:
                board[i][j] = -1
                r, c = i, j

# 도연이가 만날 수 있는 사람 수
print(get_cnt(r, c))
