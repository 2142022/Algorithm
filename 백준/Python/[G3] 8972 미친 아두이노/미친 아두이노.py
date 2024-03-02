from collections import defaultdict
import sys
input = sys.stdin.readline

# (pr, pc)에서 (r, c)와 가장 가까운 방향 구하기
def get_dir(pr, pc, r, c):
    # 가장 가까운 거리와 그 방향
    min_dist, min_dir = R + C, -1

    # 8방 탐색
    for d in range(9):
        if d == 4:
            continue
        npr, npc = pr + dr[d], pc + dc[d]
        if not (0 <= npr < R and 0 <= npc < C):
            continue
        dist = abs(npr - r) + abs(npc - c)
        if dist < min_dist:
            min_dist = dist
            min_dir = d

    return min_dir

####################################################################################

# 게임 진행
# (r, c): 종수 시작 위치
def play(r, c):
    # 종수 움직임
    for cnt, d in enumerate(move, start = 1):
        # 종수 이동
        r += dr[d]
        c += dc[d]

        # 이동 칸에 미친 아두이노가 있는 경우, 게임 끝
        if (r, c) in pos:
            return False, cnt

        # 미친 아두이노 이동
        for k, v in list(pos.items()):
            # 현재 위치 삭제
            pos[k] -= 1

            # 현재 위치
            pr, pc = k

            # 종수와 가장 가까운 방향
            d = get_dir(pr, pc, r, c)

            # 이동
            pr += dr[d]
            pc += dc[d]

            # 종수가 있는 곳이라면 게임 끝
            if (pr, pc) == (r, c):
                return False, cnt

            # 현재 위치 저장
            pos[(pr, pc)] += 1

        # 미친 아두이노가 없거나 2개 이상 있는 칸 폭발
        for k, v in list(pos.items()):
            if v != 1:
                pos.pop(k)

    # 게임이 끝난 후 종수 위치 리턴
    return True, r, c

####################################################################################

# 보드 크기
R, C = map(int, input().split())

# 종수 위치
r = c = -1
# 각 위치에 있는 미친 아두이노 개수
pos = defaultdict(int)
for i in range(R):
    row = input().rstrip()
    for j, s in enumerate(row):
        if s == 'I':
            r, c = i, j
        elif s == 'R':
            pos[(i, j)] = 1

# 종수의 움직임
move = list(map(lambda x: int(x) - 1, input().rstrip()))

# 9방 탐색
dr, dc = (1, 1, 1, 0, 0, 0, -1, -1, -1), (-1, 0, 1, -1, 0, 1, -1, 0, 1)

# 게임 결과
res = play(r, c)

# 끝까지 살아남은 경우, 보드 상태 출력
if res[0]:
    board = [['.'] * C for _ in range(R)]
    board[res[1]][res[2]] = 'I'
    for i, j in pos:
        board[i][j] = 'R'
    for i in board:
        print(''.join(i))

# 중간에 게임이 끝나는 경우, 종수가 이동한 횟수 출력
else:
    print(f'kraj {res[1]}')