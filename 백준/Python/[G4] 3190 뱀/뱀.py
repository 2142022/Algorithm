from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 보드 크기
N = int(input())
# 보드 (상단 좌측이 1행 1열이므로 0행, 0열 추가)
# 사과가 있는 곳은 1, 뱀이 있는 곳은 2
board = [[0] * (N + 1) for _ in range(N + 1)]

# 사과 개수
K = int(input())
# 사과 체크
for _ in range(K):
    i, j = map(int, input().split())
    board[i][j] = 1

# 뱀의 방향 변환 정보
L = int(input())
rotate = defaultdict(int)
for _ in range(L):
    X, C = input().rstrip().split()
    if C == 'D':
        rotate[int(X)] = 1
    else:
        rotate[int(X)] = -1

# 사방 탐색용 (상, 우, 하, 좌)
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 뱀 머리 위치, 방향
r = c = d = 1
# 뱀 있는 위치
snake = deque([(0, 0)])

# 게임 시간
time = 0

# 게임 진행
while True:
    # 방향 전환
    if time in rotate:
        d = (d + rotate[time]) % 4

    # 이동
    r += dr[d]
    c += dc[d]

    # 보드를 벗어난 경우 끝내기
    if not (1 <= r <= N and 1 <= c <= N):
        break

    # 뱀의 몸과 부딪히는 경우 끝내기
    if board[r][c] == 2:
        break

    # 사과가 없는 경우, 꼬리 위치 변경
    if board[r][c] == 0:
        tr, tc = snake.popleft()
        board[tr][tc] = 0
    # 사과 먹기
    elif board[r][c] == 1:
        board[r][c] = 0

    # 뱀 위치 갱신
    board[r][c] = 2
    snake.append((r, c))

    # 시간 증가
    time += 1

print(time + 1)