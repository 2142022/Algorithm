from collections import deque
import sys
input = sys.stdin.readline

# 각 도미노 타일에 갈 수 있는 가장 짧은 경로 구하기
def get_path():
    # 6방 탐색용
    dr, dc = (-1, 0, 1, -1, 0, 1), (-1, -2, -1, 1, 2, 1)

    # 탐색 위치를 담은 큐
    q = deque([(0, 0)])
    while q:
        # 현재 위치, 도미노 타일, 경로
        r, c = q.popleft()

        # 6방 탐색
        for d in range(6):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < 2 * N) or board[nr][nc] == 0:
                continue

            # 방문 체크
            if prev[nr][nc]:
                continue

            # 이동 가능한지 확인 (숫자가 같은지 확인)
            if d < 3:
                if board[nr][nc + 1] != board[r][c]:
                    continue
            else:
                if board[nr][nc] != board[r][c + 1]:
                    continue

            # 다음 위치 큐에 담기 (마지막 타일인 경우 끝내기)
            prev[nr][nc] = [r, c]
            if domino[nr][nc] == cnt - 1:
                return
            q.append((nr, nc))

    return

###############################################################################################

# 가장 큰 타일에 갈 수 있는 가장 짧은 경로 구하기
def get_answer():
    if N == 1:
        res.append(1)
        return

    for i in range(N - 1, -1, -1):
        # 짝수 행
        if i % 2 == 0:
            for j in range(2 * N - 2, -1, -2):
                if prev[i][j]:
                    r, c = i, j
                    while True:
                        res.append(domino[r][c])
                        r, c = prev[r][c]
                        if r == c == 0:
                            res.append(1)
                            return
        # 홀수 행
        else:
            for j in range(2 * N - 3, 0, -2):
                if prev[i][j]:
                    r, c = i, j
                    while True:
                        res.append(domino[r][c])
                        r, c = prev[r][c]
                        if r == c == 0:
                            res.append(1)
                            return

###############################################################################################

# 보드 크기
N = int(input())

# 보드
board = [[0] * (2 * N) for _ in range(N)]
# 각 칸의 도미노 타일 번호
domino = [[0] * (2 * N) for _ in range(N)]

cnt = 1
for i in range(N):
    # 짝수 행
    if i % 2 == 0:
        for j in range(N):
            board[i][2 * j], board[i][2 * j + 1] = map(int, input().split())
            domino[i][2 * j] = domino[i][2 * j + 1] = cnt
            cnt += 1
    # 홀수 행
    else:
        for j in range(1, N):
            board[i][2 * j - 1], board[i][2 * j] = map(int, input().split())
            domino[i][2 * j - 1] = domino[i][2 * j] = cnt
            cnt += 1

# 각 칸에 가기 이전 칸의 도미노 타일
prev = [[list() for _ in range(2 * N)] for _ in range(N)]
prev[0][0] = [-1, -1]
get_path()

# 가장 큰 타일에 갈 수 있는 가장 짧은 경로
res = []
get_answer()
print(len(res))
print(*reversed(res))