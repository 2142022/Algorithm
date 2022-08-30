from collections import deque
import sys
input = sys.stdin.readline

# BFS로 집 수 구하기
def bfs(r, c):
    queue = deque()
    queue.append([r,c])
    house[r][c] = 0

    # 집 수
    tmp = 0

    # 상, 하, 좌, 우를 비교
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # queue의 원소가 없을 때까지 탐색
    while queue:
        # 탐색할 행과 열 구하기
        tmp_r, tmp_c = queue.popleft()
        tmp += 1
        
        for i in range(4):
            nr = tmp_r + dr[i]
            nc = tmp_c + dc[i]

            # 집이 있는 곳이라면 queue에 추가
            if (0 <= nr < N) and (0 <= nc < N) and (house[nr][nc] == 1):
                queue.append([nr, nc])
                house[nr][nc] = 0

    return tmp

# N X N 지도
N = int(input())

# 지도
house = [list(map(int, input().strip())) for i in range(N)]

# 단지 수
cnt = 0

# 각 단지별 집 수
result = []

for i in range(N):
    for j in range(N):
        # 1이 나오면 BFS로 단지에 속하는 집의 수 구하기
        if house[i][j] == 1:
            cnt += 1
            result.append(bfs(i, j))

#출력
print(cnt)

result.sort()
for i in result:
    print(i)
