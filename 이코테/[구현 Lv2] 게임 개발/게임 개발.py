from collections import deque
import sys
input = sys.stdin.readline

# N X M 크기의 맵
N, M = map(int, input().split())

# 캐릭터의 시작 위치와 방향
x, y, dir = map(int, input().split())

# 맵 입력받기
game_map = [list(map(int, input().split())) for i in range(N)]

# 사방 탐색을 위한 dr, dc
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# BFS를 통해 시작 위치에서 연결된 육지의 개수 구하기
# 큐에 시작 위치 넣기
queue = deque()
queue.append([x, y])

# 캐릭터가 방문한 칸의 수
cnt = 0
# 방문 체크 (방문한 곳은 1로 만들기)
game_map[x][y] = 1

# 큐에 원소가 없을 때까지 반복
while queue:
    # 현재 위치 꺼내기
    r, c = queue.popleft()

    # 방문 칸 수 증가
    cnt += 1

    # 사방 탐색
    for i in range(4):
        # 다음 위치
        nr = r + dr[i]
        nc = c + dc[i]

        # 맵 범위를 벗어나면 넘어가기
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue

        # 바다거나 이미 큐에 넣은 곳은 넘어가기
        if game_map[nr][nc] == 1:
            continue

        # 방문 체크 후 큐에 위치 삽입
        game_map[nr][nc] = 1
        queue.append([nr, nc])

# 캐릭터가 총 방문한 칸 수 출력
print(cnt)
