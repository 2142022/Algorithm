import sys
input = sys.stdin.readline

# 다른 양파깡과 안 겹치는지 확인
def possible(r1, c1, r2, c2):
    for j in range(c1, c2 + 1):
        if impossible[r1][j] or impossible[r2][j]:
            return 0
    for i in range(r1 + 1, r2):
        if impossible[i][c1] or impossible[i][c2]:
            return 0
    return 1

########################################################################################################################

# M개의 양파깡 만들기
def make():
    # 양파깡 맛과 위치
    pos = []

    # M개 만들기
    for _ in range(M):
        # 최대 맛과 그 위치
        max_taste = -90000
        mr1 = mc1 = mr2 = mc2 = -1

        # 양파깡 시작 위치
        for r1 in range(1, N - 1):
            for c1 in range(1, N - 1):
                if impossible[r1][c1]:
                    continue
                # 양파깡 끝 위치
                for r2 in range(r1 + 2, N + 1):
                    for c2 in range(c1 + 2, N + 1):
                        # 현재 양파깡 맛
                        taste = (board[r2][c2] - board[r2][c1 - 1] - board[r1 - 1][c2] + board[r1 - 1][c1 - 1]) \
                                - (board[r2 - 1][c2 - 1] - board[r2 - 1][c1] - board[r1][c2 - 1] + board[r1][c1])

                        # 최대 점수와 비교
                        if taste > max_taste:
                            # 다른 양파깡과 안 겹치는지 확인
                            if not possible(r1, c1, r2, c2):
                                continue

                            max_taste = taste
                            mr1, mc1, mr2, mc2 = r1, c1, r2, c2

        # 양파깡을 만들 수 없는 경우
        if max_taste == -90000:
            return [[0]]

        # 양파깡 만들기
        pos.append((max_taste, mr1, mc1, mr2, mc2))
        for j in range(mc1, mc2 + 1):
            impossible[mr1][j] = impossible[mr2][j] = 1
        for i in range(mr1 + 1, mr2):
            impossible[i][mc1] = impossible[i][mc2] = 1

    return pos

########################################################################################################################

# 과자판 크기, 양파깡 개수
N, M = map(int, input().split())

# 과자판 (누적합)
board = [[0] * (N + 1)]
for i in range(1, N + 1):
    row = [0] + list(map(int, input().split()))
    for j in range(1, N + 1):
        row[j] += row[j - 1]
    for j in range(1, N + 1):
        row[j] += board[i - 1][j]
    board.append(row)

# 양파깡이 된 곳 체크
impossible = [[0] * (N + 1) for _ in range(N + 1)]

# 양파깡 맛과 위치
pos = make()
for p in pos:
    print(*p)