from collections import defaultdict
import sys
input = sys.stdin.readline

# 각 세대의 드래곤 커브의 방향 구하기
def find_dir():
    # 세대
    for i in range(1, MG + 1):
        # 이전 세대의 커브 방향 순서 거꾸로 한 뒤 +1
        dir[i] = dir[i - 1] + list(map(lambda x: (x + 1) % 4, dir[i - 1][::-1]))

#############################################################################################

# 이차원 좌표 평면에 드래곤 커브가 있는 곳 체크하기
def draw():
    # 사방 탐색용 (우, 상, 좌, 하)
    dr, dc = (0, -1, 0, 1), (1, 0, -1, 0)

    # 드래곤 커브
    for c, r, sd, g in curves:
        # 시작점에서부터 하나씩 그려나가기
        board[r][c] = 1

        # 현재 드래곤 커브 세대에 맞는 방향
        for d in dir[g]:
            # 초기 방향만큼 더하기
            nd = (d + sd) % 4

            # 다음 위치 찾기
            r += dr[nd]
            c += dc[nd]
            board[r][c] = 1

#############################################################################################

# 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수 구하기
def get_cnt():
    cnt = 0
    for r in range(100):
        for c in range(100):
            if board[r][c] and board[r][c + 1] and board[r + 1][c] and board[r + 1][c + 1]:
                cnt += 1
    return cnt

#############################################################################################

# 드래곤 커브 개수
N = int(input())

# 가장 높은 세대의 드래곤 커브
MG = 0

# 드래곤 커브 정보
curves = []
for _ in range(N):
    c, r, d, g = map(int, input().split())
    curves.append((c, r, d, g))
    MG = max(MG, g)

# 각 세대의 드래곤 커브의 방향 구하기
# 초기 방향은 0으로 설정 (나중에 바뀐 방향만큼 +)
dir = defaultdict(list)
dir[0] = [0]
find_dir()

# 이차원 좌표 평면에 드래곤 커브가 있는 곳 체크하기
board = [[0] * 101 for _ in range(101)]
draw()

# 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수
print(get_cnt())