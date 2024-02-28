from collections import deque
import sys
input = sys.stdin.readline

# 빌딩 탈출 시간 구하기
def escape():
    # 상근이 이동 / 불 확산
    while q:
        # 현재 위치
        r, c = q.popleft()

        # 상근이면 걸린 시간, 불이면 -1
        flag = board[r][c]

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < h and 0 <= nc < w):
                # 상근이라면 탈출
                if flag > 0:
                    return flag
                continue

            # 벽이나 불 패스
            if board[nr][nc] < 0:
                continue

            # 상근이 이동
            if flag > 0 and board[nr][nc] == 0:
                board[nr][nc] = flag + 1
                q.append((nr, nc))

            # 불 확산
            elif flag == -2:
                board[nr][nc] = flag
                q.append((nr, nc))

    # 탈출이 불가능한 경우
    return "IMPOSSIBLE"

#######################################################################################################

# 테스트 케이스
for _ in range(int(input())):
    # 지도 크기
    w, h = map(int, input().split())

    # 지도
    board = []

    # 상근이의 시작 위치
    sr, sc = -1, -1

    # 상근이나 불의 위치를 담은 큐
    q = deque()
    for i in range(h):
        row = list(map(lambda x: {'.': 0, '#': -1, '@': 1, '*': -2}[x], input().rstrip()))
        board.append(row)
        for j, c in enumerate(row):
            if c == 1:
                sr, sc = i, j
            elif c == -2:
                q.append((i, j))

    # 상근이 위치 추가
    q.appendleft((sr, sc))

    # 빌딩 탈출 시간 구하기
    print(escape())