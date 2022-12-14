import sys
input = sys.stdin.readline
from itertools import combinations

# 각 선생님마다 사방 탐색을 통해 모든 학생들이 감시로부터 피할 수 있는 지 확인
# (r, c): 선생님의 위치
# d: 탐색 방향
def check(r, c, d):
    # N(복도의 크기): 전역변수
    global N

    # 모든 학생들이 감시로부터 피할 수 있다면 YES, 아니면 NO
    result = 'YES'

    while True:
        # 탐색 위치
        r = r + dr[d]
        c = c + dc[d]

        # 복도 범위를 벗어난다면 끝내기
        if r < 0 or r >= N or c < 0 or c >= N:
            break

        # 장애물이 있다면 끝내기
        if hallway[r][c] == 'O':
            break

        # 학생이 있다면 'NO'
        if hallway[r][c] == 'S':
            result = 'NO'
            break

    return result

###############################################################################

# 복도의 크기
N = int(input().strip())
# 복도 정보
hallway = [list(input().split()) for _ in range(N)]

# 비어있는 위치 정보가 담긴 리스트
empty = [(i, j) for i in range(N) for j in range(N) if hallway[i][j] == 'X']

# 선생님 위치 정보가 담긴 리스트
teachers = [(i, j) for i in range(N) for j in range(N) if hallway[i][j] == 'T']

# 모든 학생들이 감시로부터 피할 수 있다면 YES, 아니면 NO
result = 'NO'

# 사방 탐색을 위한 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 조합을 이용하여 3개의 빈 공간에 장애물 설치하기
for obstacles in combinations(empty, 3):
    # 3개의 장애물 설치하기
    for i, j in obstacles:
        hallway[i][j] = 'O'

    # 각 선생님마다 사방 탐색을 통해 모든 학생들이 감시로부터 피할 수 있는 지 확인
    for i, j in teachers:
        for d in range(4):
            result = check(i, j, d)

            # 한 명이라도 본다면 더 이상 확인 필요X
            if result == 'NO':
                break

        # 한 명이라도 본다면 더 이상 확인 필요X
        if result == 'NO':
            break

    # 피할 수 있다면 더 이상 확인 필요X
    if result == 'YES':
        break

    # 설치한 장애물 지우기
    for i, j in obstacles:
        hallway[i][j] = 'X'

# 결과 출력
print(result)