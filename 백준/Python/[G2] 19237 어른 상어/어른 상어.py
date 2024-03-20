from collections import defaultdict
import sys
input = sys.stdin.readline

# 1번 상어만 남게 되는 시간 구하기
def get_time():
    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 최대 1000초 반복
    for time in range(1, 1001):
        # 상어 이동
        for num, pos in list(sharks.items()):
            # 현재 위치, 바라보고 있는 방향
            r, c, d = pos

            # 자신의 냄새가 있는 방향
            back = -1

            # 4방 탐색 (우선 순위에 맞게 탐색)
            for nd in D[num][d]:
                # 이동할 위치
                nr, nc = r + dr[nd], c + dc[nd]

                # 범위 체크
                if not (0 <= nr < N and 0 <= nc < N):
                    continue

                # 냄새가 있는 경우
                if board[nr][nc][0]:
                    # 다른 상어의 냄새가 있는 경우
                    if board[nr][nc][0] != num:
                        continue

                    # 본인 냄새가 있는 경우
                    elif back == -1:
                        back = nd

                # 아무 냄새도 없는 경우 이동
                else:
                    sharks[num] = [nr, nc, nd]
                    break

            # 이동을 못한 경우 본인 냄새가 있던 곳으로 이동
            else:
                nr, nc = r + dr[back], c + dc[back]
                sharks[num] = [nr, nc, back]

        # 기존에 뿌린 냄새 시간 감소
        for r in range(N):
            for c in range(N):
                if board[r][c][0]:
                    if board[r][c][1] == 1:
                        board[r][c] = [0, 0]
                    else:
                        board[r][c][1] -= 1

        # 이동한 상어의 냄새 저장
        for num, pos in sorted(list(sharks.items()), key=lambda x: x[0]):
            # 상어 위치, 방향
            r, c, d = pos

            # 이미 다른 상어가 있는 경우, 잡아먹힘
            if board[r][c][1] == k:
                sharks.pop(num)

            # 현재 상어 저장
            else:
                board[r][c] = [num, k]

        # 다른 상어가 없으면 끝내기
        if len(sharks) == 1:
            return time

    # 1000초가 넘어도 다른 상어가 있는 경우
    return -1

#################################################################################

# 격자 크기, 상어 수, 냄새 지속 시간
N, M, k = map(int, input().split())

# 격자 정보
board = [[[0, 0] for _ in range(N)] for _ in range(N)]

# 상어별 위치, 바라보는 방향
sharks = defaultdict(list)
for i in range(N):
    row = list(map(int, input().split()))
    for j, info in enumerate(row):
        if info:
            board[i][j] = [info, k]
            sharks[info] = [i, j]

# 각 상어가 바라보는 방향
for i, d in enumerate(list(map(int, input().split())), start = 1):
    sharks[i].append(d - 1)

# D[i][j]: i상어가 j방향을 바라보고 있을 때의 이동 우선 순위 방향
D = [list() for _ in range(M + 1)]
for i in range(1, M + 1):
    for _ in range(4):
        D[i].append(list(map(lambda x: int(x) - 1, input().split())))

# 1번 상어만 남게 되는 시간 구하기
print(get_time())