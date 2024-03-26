from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# (sr, sc)에서 출발에서 (er, ec)로 가는 최단 거리에서 한 칸 이동했을 때 위치 구하기
def move(sr, sc, er, ec):
    # 방문 체크
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    # 탐색 위치와 경로를 담은 큐
    q = deque([(sr, sc, [])])
    while q:
        r, c, path = q.popleft()

        # 목적지에 도착한 경우 끝내기
        if (r, c) == (er, ec):
            return path[0]

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 불가 체크
            if board[nr][nc] == -1:
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue

            # 이동
            visited[nr][nc] = 1
            # print(er, ec, path + [(nr, nc)])
            q.append((nr, nc, path + [(nr, nc)]))

###############################################################################

# (er, ec)에 있는 편의점으로 갈 수 있는 최단 거리 베이스캠프 위치 구하기
def start(er, ec):
    # 갈 수 있는 베이스 캠프와의 최단 거리
    min_dist = N * N

    # 갈 수 있는 모든 베이스 캠프
    pos = []

    # 최단 거리
    dist = [[min_dist] * N for _ in range(N)]
    dist[er][ec] = 0

    # 탐색 위치를 담은 큐
    q = deque([(er, ec)])
    while q:
        r, c = q.popleft()

        # 현재까지의 거리가 최단 거리보다 큰 경우 끝내기
        l = dist[r][c]
        if l > min_dist:
            break

        # 베이스캠프인 경우
        if board[r][c] == 1:
            min_dist = l
            pos.append((r, c))
            continue

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 불가 체크
            if board[nr][nc] == -1:
                continue

            # 방문 체크
            if dist[nr][nc] <= l + 1:
                continue

            # 이동
            dist[nr][nc] = l + 1
            q.append((nr, nc))

    # 선택된 베이스캠프
    return sorted(pos)[0]

###############################################################################

# 격자 크기, 사람 수
N, M = map(int, input().split())

# 격자 정보
board = [list(map(int, input().split())) for _ in range(N)]

# 사람별 목표 편의점
dest = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

# 사람들 위치
people = defaultdict(list)

# 목표 편의점에 도착한 사람들의 수
finish = 0

# 사방 탐색용 (상좌우하)
dr, dc = (-1, 0, 0, 1), (0, -1, 1, 0)

# 시간
time = 1
while True:
    # 사람들 한 칸씩 이동
    impossible = []
    for k, v in list(people.items()):
        r, c = v
        er, ec = dest[k]
        nr, nc = move(r, c, er, ec)

        # 도착한 경우
        if (nr, nc) == (er, ec):
            finish += 1
            people.pop(k)
            impossible.append((er, ec))

        # 이동
        else:
            people[k] = [nr, nc]

    # 점령된 편의점은 이동할 수 없음
    for r, c in impossible:
        board[r][c] = -1

    # 아직 출발할 사람이 있는 경우, 베이스캠프 찾기
    if time <= M:
        idx = time - 1
        er, ec = dest[idx]
        r, c = start(er, ec)
        people[idx] = (r, c)
        board[r][c] = -1

    # 모두 도착한 경우 끝내기
    if finish == M:
        break

    # 시간 증가
    time += 1

print(time)