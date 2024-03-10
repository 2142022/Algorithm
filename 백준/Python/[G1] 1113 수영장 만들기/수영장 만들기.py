from collections import deque
import sys
input = sys.stdin.readline

# (r, c)와 연결된 곳들 중 h 이하인 곳에 물 채우기
def fill(r, c, h):
    # 가장자리와 연결되어 있다면 물 채우기 불가
    edge = 0 if (1 <= r < N - 1 and 1 <= c < M - 1) else 1

    # 물을 채운 칸의 수
    cnt = 1
    visited[r][c] = 1

    # 탐색 위치를 담은 큐
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < M):
                edge = 1
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1

            # 물 채우기
            if H[nr][nc] <= h:
                cnt += 1
                q.append((nr, nc))

    # 가장 자리가 아닌 경우 물 채우기 가능
    return cnt * (edge ^ 1)

########################################################################################

# 직육면체 크기
N, M = map(int, input().split())

# 각 칸의 높이
H = []
# 가장 높은 높이
MH = 0
for _ in range(N):
    row = list(map(int, input().rstrip()))
    H.append(row)
    MH = max(MH, max(row))

# 수영장에 채울 물의 양
water = 0

# 가장 낮은 곳부터 채우기
for h in range(1, MH):
    # 방문 체크
    visited = [[0] * M for _ in range(N)]

    # h보다 작거나 같은 곳에 물 채우기
    for r in range(N):
        for c in range(M):
            # 아직 방문을 안 했다면, 물 채우기
            if H[r][c] <= h and not visited[r][c]:
                water += fill(r, c, h)

print(water)