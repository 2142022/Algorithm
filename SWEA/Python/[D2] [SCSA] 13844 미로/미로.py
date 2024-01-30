# DFS로 현재 위치에서 사방 탐색
def dfs(r, c):
    global N

    # 이미 도착지점까지 탐색한 경우 끝내기
    if r == D[0] and c == D[1]:
        return

    # 사방 탐색
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 현재 위치에서 사방 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != '1':
            visited[nr][nc] = 1
            dfs(nr, nc)

#################################################################################################

# 테스트케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 미로 크기
    N = int(input())

    # 미로
    maze = []
    for i in range(N):
        info = input().rstrip()
        maze.append(info)
        for j in range(N):
            # 출발지
            if info[j] == '2':
                S = (i, j)
            # 도착지
            elif info[j] == '3':
                D = (i, j)

    # 방문 체크
    visited = [[0] * N for _ in range(N)]
    visited[S[0]][S[1]] = 1

    # DFS로 탐색
    dfs(S[0], S[1])

    print(f'#{t} {visited[D[0]][D[1]]}')