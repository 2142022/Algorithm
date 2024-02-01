import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 게임 맵 크기
    H, W = map(int, input().split())

    # 전차의 방향에 따른 숫자
    dir = {'^': 0, 'v': 1, '<': 2, '>': 3}

    # 게임 맵
    board = []
    # 전차의 위치, 방향
    r = c = d = -1
    for i in range(H):
        row = list(input().rstrip())
        board.append(row)
        if r == -1:
            for j, info in enumerate(row):
                if info in dir:
                    r, c, d = i, j, dir[info]
                    board[r][c] = '.'

    # 사용자 입력 개수
    N = int(input())

    # 사용자 입력 (U: 0, D: 1, L: 2, R: 3, S: 4)
    order = list(map(lambda x: {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4}[x], input().rstrip()))

    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 사용자 입력 하나씩 실행하기
    for op in order:
        # 한 칸 이동하기
        if op < 4:
            d = op
            if 0 <= r + dr[d] < H and 0 <= c + dc[d] < W and board[r + dr[d]][c + dc[d]] == '.':
                r += dr[d]
                c += dc[d]

        # 포탄 쏘기
        else:
            # 포탄의 위치
            pr, pc = r, c
            while True:
                pr += dr[d]
                pc += dc[d]

                # 범위를 벗어난 경우
                if not (0 <= pr < H and 0 <= pc < W):
                    break

                # 벽을 만난 경우
                if board[pr][pc] in ('*', '#'):
                    if board[pr][pc] == '*':
                        board[pr][pc] = '.'
                    break

                # 물이 아니라면 평지로 바꾸기
                if board[pr][pc] != '-':
                    board[pr][pc] = '.'

    # 전차의 마지막 위치 맵에 표시하기
    board[r][c] = {0: '^', 1: 'v', 2: '<', 3: '>'}[d]

    # 최종 게임 맵 출력
    print(f'#{t}', end = ' ')
    for b in board:
        print(''.join(b))
