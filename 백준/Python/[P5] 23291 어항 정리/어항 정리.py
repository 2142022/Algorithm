from collections import defaultdict
import sys
input = sys.stdin.readline

# 공중 부양 작업: 2개 이상 쌓인 어항 90도 회전 후, 쌓기
def build1():
    global board, new

    while True:
        # 회전할 어항 추가
        new.append(board[:len(new[0])])
        board = board[len(new[0]):]

        # 회전했을 때 공중에 떠 있는 어항이 생긴다면 끝내기
        if len(new) > len(board):
            new[-1] += board
            break

        # 시계방향으로 90도 회전
        new = list(map(list, zip(*new[::-1])))

#################################################################################################

# 물고기 수 조절
def change():
    # 각 어항의 물고기 수 변화량
    plus = defaultdict(int)

    # 어항
    for i in range(len(new)):
        for j in range(len(new[i])):
            # 현재 칸의 물고기 수
            origin = new[i][j]

            # 총 감소시킬 수
            minus = 0

            # 4방 탐색
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                # 범위 체크
                if not (0 <= ni < len(new) and 0 <= nj < len(new[ni])):
                    continue

                # 차이를 5로 나눴을 때 양수인 경우만 이동
                d = (origin - new[ni][nj]) // 5
                if d > 0:
                    minus += d
                    plus[(ni, nj)] += d

            # 현재 칸 감소
            plus[(i, j)] -= minus

    # 모든 어항의 물고기 수 변화
    for k, v in plus.items():
        i, j = k
        new[i][j] += v

#################################################################################################

# 일렬로 놓기
def rearrange():
    global new, board

    board = []

    # 2개 이상 쌓인 어항 시계 방향으로 90도 회전 후 저장
    plus = list(map(list, zip(*new[::-1])))
    for p in plus:
        board += p

    # 나머지 추가
    board += new[-1][len(new[-2]):]

#################################################################################################

# 공중 부양 작업: 왼쪽 반을 180도 회전 후, 쌓기
def build2():
    global board, new

    # 좌우 반으로 나눈 후, 왼쪽을 180도 회전해서 위로 쌓기
    board = [board[:len(board) // 2][::-1], board[len(board) // 2:]]

    # 다시 좌우 반으로 나눈 후, 왼쪽을 180도 회전해서 위로 쌓기
    up, down = [b[:len(board[0]) // 2] for b in board], [b[len(board[0]) // 2:] for b in board]
    for _ in range(2):
        up = list(map(list, zip(*up[::-1])))
    new = up + down

#################################################################################################

# 어항 수, 물고기 차이 수 기준
N, K = map(int, input().split())

# 각 어항의 물고기 수
board = list(map(int, input().split()))

# 정리 횟수
cnt = 0
while True:
    # 최소 물고기와 최대 물고기 수 차이
    min_cnt = min(board)
    if max(board) - min_cnt <= K:
        print(cnt)
        break

    # 가장 작은 물고기 수를 가진 어항에 +1
    for i, b in enumerate(board):
        if b == min_cnt:
            board[i] += 1

    # 공중 부양 작업: 2개 이상 쌓인 어항 90도 회전 후, 쌓기
    # 회전할 어항, 바닥에 있는 어항
    new, board = [[board[0]]], board[1:]
    build1()

    # 물고기 수 조절
    change()

    # 일렬로 놓기
    rearrange()

    # 공중 부양 작업: 왼쪽 반을 180도 회전 후, 쌓기
    build2()

    # 물고기 수 조절
    change()

    # 일렬로 놓기
    rearrange()

    cnt += 1