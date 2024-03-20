from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 가장 가까운 사람의 위치와 이동 거리 찾기
def find(r, c, T):
    # 현재 위치에 사람이 있는 경우
    if board[r][c] == 2:
        return r, c, 0

    # 방문 체크 (이동 거리 저장)
    visited = [[0] * N for _ in range(N)]

    # 태울 수 있는 사람의 거리, 위치
    possible = []

    # 탐색 위치를 담은 큐
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        t = visited[r][c]

        # 연료를 다 쓴 경우 끝내기
        if t == T:
            break

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue
            visited[nr][nc] = t + 1

            # 벽이 있는 경우 패스
            if board[nr][nc] == 1:
                continue

            # 빈 칸인 경우
            if board[nr][nc] == 0:
                q.append((nr, nc))

            # 승객이 있는 경우
            else:
                possible.append((nr, nc, t + 1))
                q.append((nr, nc))

    # 태운 사람이 없는 경우
    if not possible:
        return -1, -1, -1
    else:
        return sorted(possible, key = lambda x: (x[2], x[0], x[1]))[0]

############################################################################

# 현재 손님을 목적지까지 이동시는데 드는 연료 양 구하기
def move(sr, sc, T):
    # 목적지
    er, ec = destination[(sr, sc)]

    # 연료보다 거리가 먼 경우
    if abs(er - sr) + abs(ec - sc) > T:
        return -1, -1, -1

    # 방문 체크 (이동 거리 저장)
    visited = [[0] * N for _ in range(N)]

    # 탐색 위치를 담은 큐
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        t = visited[r][c]

        # 더 이상 이동할 수 없는 경우 끝내기
        if t == T:
            break

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 목적지인 경우 끝
            if nr == er and nc == ec:
                return nr, nc, t + 1

            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue
            visited[nr][nc] = t + 1

            # 벽이 있는 경우 패스
            if board[nr][nc] == 1:
                continue

            # 이동
            q.append((nr, nc))

    # 목적지까지 갈 수 없는 경우
    return -1, -1, -1

############################################################################

# 모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양 구하기
def work(r, c, T):
    while True:
        # 모든 손님을 이동시킨 경우
        if not destination:
            return T

        # 가장 가까운 사람의 위치와 이동 거리 찾기
        r, c, t = find(r, c, T)

        # 아무도 이동시키지 못하는 경우
        if r == -1:
            return -1

        # 연료 감소 & 출발지 삭제
        T -= t
        board[r][c] = 0

        # 현재 손님을 목적지까지 이동시는데 드는 연료 양
        nr, nc, t = move(r, c, T)

        # 현재 손님을 이동시키지 못한 경우
        if nr == -1:
            return -1

        # 소모한 연료만큼 추가 & 승객 지우기
        T += t
        destination.pop((r, c))
        r, c = nr, nc

############################################################################

# 지도 크기, 승객 수, 연료 양
N, M, T = map(int, input().split())

# 지도
board = [list(map(int, input().split())) for _ in range(N)]

# 택시 출발 위치
r, c = map(lambda x: int(x) - 1, input().split())

# 각 승객의 출발지에 대한 목적지
destination = defaultdict(tuple)
for _ in range(M):
    sr, sc, er, ec = map(lambda x: int(x) - 1, input().split())
    board[sr][sc] = 2
    destination[(sr, sc)] = (er, ec)

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양
print(work(r, c, T))