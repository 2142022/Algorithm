from collections import defaultdict
import sys
input = sys.stdin.readline

# 플레이
# (r, c): 캐릭터 위치
def play(r, c):
    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 플레이어 입력 방향
    for d in move:
        # 다음 위치
        nr, nc = r + dr[d], c + dc[d]

        # 벽 패스
        if board[nr][nc] == -1:
            continue

        # 빈 칸: 캐릭터 이동
        elif board[nr][nc] == 0:
            r, c = nr, nc

        # 박스
        else:
            # 다다음 위치
            nnr, nnc = nr + dr[d], nc + dc[d]

            # 다다음에 벽이나 다른 박스가 있는 경우 이동 불가
            if board[nnr][nnc] != 0:
                continue

            # 박스 및 캐릭터 이동
            board[nnr][nnc] = 1
            if (nnr, nnc) in des:
                des[(nnr, nnc)] = 1
            board[nr][nc] = 0
            if (nr, nc) in des:
                des[(nr, nc)] = 0
            r, c = nr, nc

            # 모든 박스가 목표점에 도달한 경우 끝내기
            if sum(des.values()) == len(des):
                return True, r, c

    # 종료 여부 및 캐릭터 마지막 위치 반환
    return sum(des.values()) == len(des), r, c

###############################################################################################

# 테스트 케이스
TC = 0
while True:
    TC += 1

    # 게임 크기
    R, C = map(int, input().split())

    # 0, 0인 경우 끝내기
    if R == C == 0:
        break

    # 게임 정보 (벽: -1, 빈 공간: 0, 박스: 1)
    board = [[0] * C for _ in range(R)]
    # 목표점에 박스 존재 여부 체크
    des = defaultdict(int)
    # 캐릭터 위치
    r = c = 0

    # 입력받기
    for i in range(R):
        row = input().rstrip()
        for j, info in enumerate(row):
            if info == '.':
                continue
            elif info == '#':
                board[i][j] = -1
            elif info == '+':
                des[(i, j)] = 0
            elif info == 'b':
                board[i][j] = 1
            elif info =='B':
                board[i][j] = 1
                des[(i, j)] = 1
            elif info == 'w':
                r, c = i, j
            elif info == 'W':
                r, c = i, j
                des[(i, j)] = 0

    # 플레이어 입력
    move = list(map(lambda x: {'U': 0, 'D': 1, 'L': 2, 'R': 3}[x], input().rstrip()))

    # 플레이
    complete, r, c = play(r, c)

    # 보드 바꾸기
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                if (i, j) in des:
                    board[i][j] = 'W' if (r, c) == (i, j) else '+'
                elif r == i and c == j:
                    board[i][j] = 'w'
                else:
                    board[i][j] = '.'
            elif board[i][j] == -1:
                board[i][j] = '#'
            else:
                board[i][j] = 'B' if (i, j) in des else 'b'

    # 게임 종료 여부
    if complete:
        print(f'Game {TC}: complete')
    else:
        print(f'Game {TC}: incomplete')

    # 게임 상태 출력
    for b in board:
        print(''.join(b))