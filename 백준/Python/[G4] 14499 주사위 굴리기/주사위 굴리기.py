import sys
input = sys.stdin.readline

# 주사위 돌리기
# d: 방향
def change(d):
    # 동쪽으로 회전
    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]

    # 서쪽으로 회전
    elif d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]

    # 북쪽으로 회전
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    # 남쪽으로 회전
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

#####################################################################################

# 지도 크기, 주사위 좌표, 명령 수
N, M, r, c, K = map(int, input().split())

# 지도 정보
board = [list(map(int, input().split())) for _ in range(N)]

# 이동 순서
order = list(map(lambda x: int(x) - 1, input().split()))

# 주사위의 각 칸에 쓰여있는 숫자
# 첫 번째 원소가 윗면, 마지막 원소가 아랫면
dice = [0] * 6

# 사방 탐색용 (오, 왼, 상, 하)
dr, dc = (0, 0, -1, 1), (1, -1, 0, 0)

# 이동하기
for d in order:
    # 다음 위치
    nr, nc = r + dr[d], c + dc[d]

    # 이동이 불가능한 경우, 패스
    if not (0 <= nr < N and 0 <= nc < M):
        continue

    # 이동하기
    r, c = nr, nc

    # 주사위 돌리기
    change(d)

    # 이동하는 칸에 쓰여진 수가 0인 경우, 주사위 바닥면에 있는 수 복사
    if board[r][c] == 0:
        board[r][c] = dice[5]

    # 이동하는 칸에 쓰여진 수가 0이 아닌 경우, 칸에 쓰여진 수가 주사위 바닥면으로 복사 + 칸은 0
    else:
        dice[5] = board[r][c]
        board[r][c] = 0

    # 주사위 윗면 출력
    print(dice[0])