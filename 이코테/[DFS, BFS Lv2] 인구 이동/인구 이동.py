from collections import deque
import sys
input = sys.stdin.readline

# 연합 구하는 함수(BFS)
def team(r, c):
    global order, N, L, R

    queue = deque()
    queue.append([r, c])
    flag[r][c] = order

    while queue:
        tmp_r, tmp_c = queue.popleft()

        for i in range(4):
            nr = tmp_r + dr[i]
            nc = tmp_c + dc[i]

            # 연합이라면 flag에 체크
            if (0 <= nr < N) and (0 <= nc < N) and (L <= abs(A[nr][nc] - A[tmp_r][tmp_c]) <= R):
                # 연합 추가
                if flag[nr][nc] == 0:
                    queue.append([nr, nc])
                    flag[nr][nc] = order
            

N, L, R = map(int, input().split())

# N X N 크기의 땅과 각 나라 인구수
A = [list(map(int, input().split())) for i in range(N)]

# 인구 이동하는 날 수
cnt = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while True:
    # 몇 번째 연합인지
    order = 0

    # 연합인지 체크
    flag = [[0] * N for i in range(N)]

    # 연합 구하기
    for i in range(N):
        for j in range(N):
            # 이미 연합이라면 패스
            if flag[i][j]:
                continue

            # 연합이 있으면 구하기
            for k in range(4):
                if (0 <= i + dr[k] < N) and (0 <= j + dc[k] < N) and (L <= abs(A[i + dr[k]][j + dc[k]] - A[i][j]) <= R):
                    order += 1
                    team(i, j)
                    break

    # 연합이 없으면 끝내기
    if order == 0:
        break
    else:
        cnt += 1
        
    # 인구이동
    for n in range(1, order + 1):
        # 연합의 인구 수
        population = 0

        # 연합 국가 수
        nation = 0

        # 연합 국가의 총 인구 수와 국가 수 구하기
        for i in range(N):
            for j in range(N):
                if flag[i][j] == n:
                    population += A[i][j]
                    nation += 1

        tmp = population // nation

        # 인구 이동   
        for i in range(N):
            for j in range(N):
                if flag[i][j] == n:
                    A[i][j] = tmp
                    
print(cnt)
