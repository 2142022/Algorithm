import sys
input = sys.stdin.readline
from itertools import combinations
import copy

# board: N X M 크기의 지도
N, M = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸 위치 정보가 담긴 리스트
empty = [(i, j) for i in range(N) for j in range(M) if origin_board[i][j] == 0]

# 사방 탐색을 위한 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 최대 안전 영역의 크기
max_cnt = 0

# 조합을 이용하여 3개의 빈 칸에 벽 세우기
for wall in combinations(empty, 3):
    # 맵이 변경되므로 복사해서 사용하기
    board = copy.deepcopy(origin_board)

    # 3개의 벽 세우기
    for i, j in wall:
        board[i][j] = 1

    # 바이러스의 위치 정보가 담긴 리스트
    virus = [(i, j) for i in range(N) for j in range(M) if origin_board[i][j] == 2]

    # virus에 원소가 없어질 때가지 반복
    while virus:
        # 바이러스 위치 정보 뽑기
        r, c = virus.pop()

        # 사방 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # board 범위를 벗어나면 패스
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 바이러스 주변에 빈 칸이 있다면 바이러스로 바꾸고 virus에 추가
            if board[nr][nc] == 0:
                board[nr][nc] = 1
                virus.append((nr, nc))

    # 안전 영역의 크기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1

    # 최대 안전 영역의 크기와 비교하기
    max_cnt = max(max_cnt, cnt)

# 최대 안전 영역의 크기 출력
print(max_cnt)