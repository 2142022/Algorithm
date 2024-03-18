from collections import deque
import sys
input = sys.stdin.readline

# (i, j)부터 시작하는 블록 그룹 찾기
def get_group(i, j):
    # 현재 블록 수
    num = board[i][j]

    # 그룹 내 블록 위치
    pos = [(i, j)]

    # 방문 체크
    visited[i][j] = 1

    # 무지개 블록
    rainbow = set()

    # 탐색 위치를 담은 큐
    q = deque([(i, j)])
    while q:
        r, c = q.popleft()

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 같은 블록인 경우
            if board[nr][nc] == num and not visited[nr][nc]:
                visited[nr][nc] = 1
                pos.append((nr, nc))
                q.append((nr, nc))

            # 무지개 블록인 경우
            if board[nr][nc] == 0 and (nr, nc) not in rainbow:
                rainbow.add((nr, nc))
                pos.append((nr, nc))
                q.append((nr, nc))

    return pos, len(rainbow)

#################################################################################

# 크기가 가장 큰 블록 그룹 찾기 & 제거
def find():
    global visited

    # 가장 큰 블록 그룹
    max_group = []
    # 가장 큰 블록 그룹의 무지개 블록 개수
    max_rainbow = 0

    # 방문 체크
    visited = [[0] * N for _ in range(N)]

    # 기준 블록
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                group, rainbow = get_group(i, j)

                # 가장 큰 블록 그룹과 비교
                if len(group) > len(max_group):
                    max_group = group[:]
                    max_rainbow = rainbow
                elif len(group) == len(max_group) and rainbow >= max_rainbow:
                        max_group = group[:]
                        max_rainbow = rainbow

    # 가장 큰 블록이 없는 경우
    if len(max_group) < 2:
        return 0

    # 블록 그룹 내의 모든 블록 제거
    for i, j in max_group:
        board[i][j] = -2
    # print(max_group, max_rainbow)
    return len(max_group)

#################################################################################

# 모든 블럭 아래로 이동
def down():
    # 열
    for j in range(N):
        # 이동 후의 블록
        column = []

        # 행
        for i in range(N - 1, -1, -1):
            num = board[i][j]
            # 무지개, 일반 블록 넣기
            if num >= 0:
                column.append(num)

            # 검정 블록인 경우, 필요한 만큼 -2로 채운 후 검정 블록 넣기
            elif num == -1:
                column += [-2] * (N - i - 1 - len(column)) + [-1]

        # 나머지는 -2로 채우기
        column += [-2] * (N - len(column))

        # 결과 저장
        for i in range(N):
            board[i][j] = column.pop()

#################################################################################

# 격자 크기, 색상 개수
N, M = map(int, input().split())

# 격자
board = [list(map(int, input().split())) for _ in range(N)]

# 최종 점수
score = 0

# 블록 그룹이 존재하는 동안 반복
while True:
    # 크기가 가장 큰 블록 그룹 찾기 & 제거
    B = find()

    # 블록 그룹이 없는 경우 끝내기
    if B == 0:
        break

    # 점수 갱신
    score += B * B

    # 중력 작용
    down()

    # 반시계 방향 90도 회전 후 중력 작용
    board = list(map(list, zip(*board)))[::-1]
    down()

print(score)