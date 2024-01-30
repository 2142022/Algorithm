import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 현재 위치 (r, c)에서 사방 탐색
def dfs(r, c):
    global N, M

    # 사방 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and field[nr][nc]:
            field[nr][nc] = 0
            dfs(nr, nc)

#########################################################################################

# 테스트 케이스
for _ in range(int(input())):
    # 배추밭의 가로, 세로 길이, 배추 개수
    M, N, K = map(int, input().split())

    # 배추 위치
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        field[i][j] = 1

    # 필요한 최소 배추흰지렁이 수
    cnt = 0

    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 배추가 인접해있는 구역의 시작점 찾기
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                field[i][j] = 0
                cnt += 1

                # DFS로 인접해 있는 배추 방문 체크
                dfs(i, j)

    print(cnt)
