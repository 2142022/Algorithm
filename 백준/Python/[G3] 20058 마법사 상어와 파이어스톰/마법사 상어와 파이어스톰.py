from collections import deque
import sys
input = sys.stdin.readline

# l단계 파이어스톰
def firestorm(l):
    # 부분 격자의 크기
    n = 2 ** l

    # 부분 격자의 시작점
    for i in range(0, T, n):
        for j in range(0, T, n):
            # 현재 부분 격자를 시계 방향으로 90도 회전
            grid = list(map(list, zip(*[a[j:j + n] for a in A[i:i + n]][::-1])))

            # 원래 배열에 저장
            for r in range(n):
                A[i + r][j:j + n] = grid[r]

#############################################################################################

# 얼음과 인접한 칸이 3개 이상 없다면, 얼음 양 -1
def melt():
    # 얼음이 줄어드는 칸
    pos = []

    # 모든 칸 탐색
    for r in range(T):
        for c in range(T):
            # 현재 칸에 얼음이 있는 경우만 확인
            if A[r][c]:
                # 얼음과 인접한 칸의 개수
                cnt = 0

                # 사방 탐색
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]

                    # 범위 체크
                    if not (0 <= nr < T and 0 <= nc < T):
                        continue

                    # 얼음 확인
                    if A[nr][nc]:
                        cnt += 1

                # 사방에 얼음이 3칸 이상 없다면 -1
                if cnt < 3:
                    pos.append((r, c))

    # 얼음 양 감소
    for r, c in pos:
        A[r][c] -= 1

#############################################################################################

# (r, c)에서부터 시작하는 덩어리 크기 구하기
def get_cnt(r, c):
    global ice

    # 덩어리 크기
    cnt = 1
    visited[r][c] = 1
    ice += A[r][c]

    # 탐색 위치를 담은 큐
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < T and 0 <= nc < T):
                continue

            # 얼음 확인
            if A[nr][nc] and not visited[nr][nc]:
                cnt += 1
                ice += A[nr][nc]
                visited[nr][nc] = 1
                q.append((nr, nc))

    return cnt

#############################################################################################

# 격자 크기, 파이어 스톰 시전 횟수
N, Q = map(int, input().split())

# 총 격자 크기
T = 2 ** N

# 얼음 양
A = [list(map(int, input().split())) for _ in range(T)]

# 파이어스톰 단계
L = list(map(int, input().split()))

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 파이어스톰 단계
for l in L:
    # 파이어스톰
    firestorm(l)

    # 줄어드는 칸 확인
    melt()

# 남아있는 총 얼음 양
ice = 0

# 가장 큰 덩어리 크기
max_cnt = 0

# 방문 체크
visited = [[0] * T for _ in range(T)]

# 덩어리 시작점
for i in range(T):
    for j in range(T):
        # 현재 덩어리 크기 구하기
        if A[i][j] and not visited[i][j]:
            max_cnt = max(max_cnt, get_cnt(i, j))

print(ice, max_cnt, sep = '\n')
