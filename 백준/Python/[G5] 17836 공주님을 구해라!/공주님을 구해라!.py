from collections import deque
import sys
input = sys.stdin.readline

# 성의 크기: N X M, T: 공주에게 걸린 저주의 제한 시간
N, M, T = map(int, input().split())

# 성의 정보
castle = [list(map(int, input().split())) for _ in range(N)]

# 방문한 곳이라면 True
visit = [[False] * M for _ in range(N)]

# 사방 탐색용
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 공주를 구하는 최단 시간
result = 2147483647

# 현재 위치, 현재까지 걸린 시간 정보를 담은 큐
q = deque()
q.append((0, 0, 0))

# 큐가 빌 때까지 반복
while q:
    # (r, c): 현재 위치, t: 현재까지 걸린 시간
    r, c, t = q.popleft()

    # 사방 탐색
    for i in range(4):
        # 다음 위치
        nr = r + dr[i]
        nc = c + dc[i]

        # 성의 범위를 벗어나는 경우 패스
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        # 공주님이 있는 곳이라면 거리 비교
        if nr == N - 1 and nc == M - 1:
            result = min(result, t + 1)
            continue

        # 그람이 있는 경우, 그람 획득
        # 그람을 획득하면 어디든 갈 수 있으므로 바로 공주님이 있는 위치와의 거리 계산
        if castle[nr][nc] == 2:
            visit[nr][nc] == True
            result = min(result, (t + 1) + (N - 1 - nr) + (M - 1 - nc))

        # 아직 방문하지 않았으며 갈 수 있는 곳이고, 제한 시간 이내라면 큐에 추가
        elif castle[nr][nc] == 0 and t + 1 <= T and visit[nr][nc] == False:
            visit[nr][nc] = True
            q.append((nr, nc, t + 1))

# 저주 제한 시간 이내에 공주를 만난 경우
if result <= T:
    print(result)
else:
    print("Fail")