import sys
input = sys.stdin.readline

# 사방 탐색을 위한 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 합의 최댓값 구하기
# idx: 현재까지 더한 칸 수
# now: 현재까지 더한 합
def getMaxSum(idx, now):
    # 4개를 모두 구한 경우
    if idx == 4:
        global max_sum
        max_sum = max(max_sum, now)
        return

    # 현재 구한 3개에 최대 숫자를 더해도 최댓값보다 작은 경우
    # 시간을 줄이기 위함
    if idx == 3 and now + max_num <= max_sum:
        return

    # 다음 위치 찾기
    for (r, c) in select:
        for d in range(4):
            # 다음 위치
            nr = r + dr[d]
            nc = c + dc[d]

            # 종이 위에 있는지 확인
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 이미 방문했는지 체크
            if visit[nr][nc] == True:
                continue

            # 방문 체크 후 재귀적으로 구하기
            visit[nr][nc] = True
            select.append((nr, nc))
            getMaxSum(idx + 1, now + paper[nr][nc])

            # 방문 체크 취소
            visit[nr][nc] = False
            select.remove((nr, nc))

###################################################################

# N X M 크기의 종이
N, M = map(int, input().split())

# 종이 위의 각 칸의 수와 최대 숫자 구하기
paper = []
max_num = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    max_num = max(max_num, max(tmp))
    paper.append(tmp)

# 테트로미노에는 4개의 정사각형을 이어붙일 수 있는 모든 경우의 수가 있으므로
# 연속된 4개를 더해서 가장 큰 합을 구하기

# 방문 체크
visit = [[False] * M for _ in range(N)]

# 최대값
max_sum = 0

# 합의 최대값 구하기
for i in range(N):
    for j in range(M):
        # 현재 더한 칸의 위치 정보를 담은 리스트
        select = []
        select.append((i, j))
        visit[i][j] = True
        getMaxSum(1, paper[i][j])
        visit[i][j] = False

print(max_sum)