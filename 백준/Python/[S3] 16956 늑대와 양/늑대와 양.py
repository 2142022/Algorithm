import sys
input = sys.stdin.readline

# 목장의 크기: R X C
R, C = map(int, input().split())

# 목장 정보
pasture = [list(input().rstrip()) for _ in range(R)]

# 울타리를 설치했을 때 늑대를 막을 수 있다면 1, 아니면 0
possible = 1

# 상하좌우 탐색용
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 양의 상하좌우에 울타리 설치하기
for i in range(R):
    for j in range(C):
        # 양이 있는 경우
        if pasture[i][j] == 'S':
            # 인접한 상하좌우에 늑대가 있으면 불가능
            for k in range(4):
                # 목장의 범위에 들어있는 경우만 확인
                if 0 <= i + dr[k] < R and 0 <= j + dc[k] < C:
                    # 늑대가 있는 경우
                    if pasture[i + dr[k]][j + dc[k]] == 'W':
                        possible = 0
                        break
                    # 양이 있는 경우
                    elif pasture[i + dr[k]][j + dc[k]] == 'S':
                        continue
                    # 울타리 설치
                    else:
                        pasture[i + dr[k]][j + dc[k]] = 'D'

        # 이미 불가능하다고 판단되면 끝내기
        if possible == 0:
            break
    # 이미 불가능하다고 판단되면 끝내기
    if possible == 0:
        break

# 결과 출력
print(possible)
if possible == 1:
    for i in range(R):
        for j in range(C):
            print(pasture[i][j], end = '')
        print()