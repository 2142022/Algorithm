import sys
input = sys.stdin.readline

# DFS로 경우의 수 구하기
# (r, c): 현재 위치, idx: 현재 방문해야 하는 칸의 인덱스
def dfs(r, c, idx):
    global n, m, cnt

    # 방문 지점에 도착한 경우
    if r == destination[idx][0] and c == destination[idx][1]:
        # 최종 방문 지점인 경우, 경우의 수 증가
        if idx == m - 1:
            cnt += 1
            return
        else:
            # 사방 탐색
            for i in range(4):
                # 다음 위치
                nr = r + dr[i]
                nc = c + dc[i]

                # 범위를 벗어나거나 벽이거나 이미 방문한 곳은 패스
                if not (0 <= nr < n and 0 <= nc < n) or graph[nr][nc] or visited[nr][nc]:
                    continue
                
                # 방문체크
                visited[nr][nc] = 1

                # DFS로 다음 위치 가기
                dfs(nr, nc, idx + 1)

                # 방문체크 취소
                visited[nr][nc] = 0

    # 아직 방문 지점에 도착하지 못한 경우
    else:
        # 사방 탐색
        for i in range(4):
            # 다음 위치
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위를 벗어나거나 벽이거나 이미 방문한 곳은 패스
            if not (0 <= nr < n and 0 <= nc < n) or graph[nr][nc] or visited[nr][nc]:
                continue

            # 방문체크
            visited[nr][nc] = 1

            # DFS로 다음 위치 가기
            dfs(nr, nc, idx)

            # 방문체크 취소
            visited[nr][nc] = 0

#################################################################################################

# n: 격자 크기, m: 방문해야 하는 칸 수
n, m = map(int, input().split())

# 격자
graph = [list(map(int, input().split())) for _ in range(n)]

# 순서대로 방문해야 하는 칸
destination = []
for _ in range(m):
    r, c = map(int, input().split())
    destination.append((r - 1, c - 1))

# 방문 체크용
visited = [[0] * n for _ in range(n)]
visited[destination[0][0]][destination[0][1]] = 1

# 사방 탐색용
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 방문 가능한 경우의 수
cnt = 0

# DFS로 경우의 수 구하기
dfs(destination[0][0], destination[0][1], 1)

# 경우의 수 출력
print(cnt)