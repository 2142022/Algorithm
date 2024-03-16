from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 게임 진행
def play():
    # 게임 시간
    time = 1

    # 뱀 머리 위치, 방향
    r, c, d = 0, 0, 0
    board[r][c] = 1

    # 사방 탐색 (우, 하, 좌, 상)
    dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)

    # 뱀의 몸의 위치를 담은 큐
    pos = deque([(0, 0)])

    # 게임 진행
    while True:
        # 뱀 머리 이동
        r += dr[d]
        c += dc[d]

        # 벽을 만난 경우 끝내기
        if not (0 <= r < N and 0 <= c < N):
            return time

        # 자신의 몸이 있는 경우 끝내기
        if board[r][c] == 1:
            return time

        # 사과가 없는 경우 꼬리 이동
        if board[r][c] == 0:
            pr, pc = pos.popleft()
            board[pr][pc] = 0

        # 현재 위치 저장
        pos.append((r, c))
        board[r][c] = 1

        # 뱀 회전
        d = (d + T[time]) % 4

        # 시간 증가
        time += 1

###############################################################

# 보드 크기
N = int(input())

# 보드
board = [[0] * N for _ in range(N)]

# 사과 수
K = int(input())

# 사과 체크
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 2

# 뱀의 방향 변환 횟수
L = int(input())

# 뱀의 방향 변환 정보
T = defaultdict(int)
for _ in range(L):
    X, D = input().split()
    if D == 'L':
        T[int(X)] = -1
    else:
        T[int(X)] = 1

# 게임이 몇 초에 끝나는지 출력
print(play())