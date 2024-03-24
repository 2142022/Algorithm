from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# (i, j)에서부터 시작한 그룹에 g 저장
# num: 원래 격자에서의 숫자
def find_group(i, j, g, num):
    G[i][j] = g

    # 현재 그룹의 칸 수
    area = 1

    # 탐색 위치를 담은 큐
    q = deque([(i, j)])
    while q:
        r, c = q.popleft()

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 체크
            if G[nr][nc]:
                continue

            # 격자에서의 숫자가 같은 경우 같은 그룹
            if board[nr][nc] == num:
                G[nr][nc] = g
                area += 1
                q.append((nr, nc))

    return area

################################################################################

# 예술 점수 구하기
def get_score():
    global G

    # 그룹별 칸 수, 원래 숫자
    group = defaultdict(list)

    # 새로운 그룹 숫자를 저장
    G = [[0] * N for _ in range(N)]

    # 그룹 숫자
    cnt = 1
    for i in range(N):
        for j in range(N):
            # 새로운 그룹 시작
            if not G[i][j]:
                num = board[i][j]
                area = find_group(i, j, cnt, num)
                group[cnt] = [area, num]
                cnt += 1

    # 각 그룹쌍별 맞닿은 변 개수
    line = defaultdict(int)
    for i in range(N):
        for j in range(N):
            # 현재 그룹
            g1 = G[i][j]

            # 오른쪽, 아래 탐색
            for ni, nj in ((i, j + 1), (i + 1, j)):
                # 범위 체크
                if not (0 <= ni < N and 0 <= nj < N):
                    continue

                # 다른 그룹인 경우 맞닿은 변 개수 추가
                g2 = G[ni][nj]
                if g1 != g2:
                    line[(min(g1, g2), max(g1, g2))] += 1

    # 예술 점수 구하기
    score = 0
    for groups, line_cnt in line.items():
        g1, g2 = groups
        g1_cnt, g1_num = group[g1]
        g2_cnt, g2_num = group[g2]
        score += (g1_cnt + g2_cnt) * g1_num * g2_num * line_cnt
    return score

################################################################################

# 회전
def rotate(board):
    # 현재 보드 반시계 방향으로 90도 회전
    new = list(map(list, zip(*board)))[::-1]

    # 십자 모양을 제외한 나머지 부분 시계 방향으로 90도 회전
    M = N // 2
    one = list(map(list, zip(*[b[:M] for b in board[:M]][::-1])))
    two = list(map(list, zip(*[b[M + 1:] for b in board[:M]][::-1])))
    three = list(map(list, zip(*[b[:M] for b in board[M + 1:]][::-1])))
    four = list(map(list, zip(*[b[M + 1:] for b in board[M + 1:]][::-1])))

    # 보드 갱신
    for i in range(M):
        board[i] = one[i] + [new[i][M]] + two[i]
        board[i + M + 1] = three[i] + [new[i + M + 1][M]] + four[i]
    board[M] = new[M]

    return board

################################################################################

# 격자 크기
N = int(input())

# 격자
board = [list(map(int, input().split())) for _ in range(N)]

# 총 예술점수 (초기 예술 점수로 초기화)
score = get_score()

# 3번 회전
for _ in range(3):
    # 회전
    board = rotate(board)

    # 예술점수 구하기
    score += get_score()

print(score)