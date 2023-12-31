from collections import deque
import sys
input = sys.stdin.readline

# 땅 크기, 최소 인구 차이, 최대 인구 차이
N, L, R = map(int, input().split())

# N X N 크기의 땅과 각 나라 인구수
A = [list(map(int, input().split())) for _ in range(N)]

# 인구 이동 일수
day = 0

# 사방 탐색
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 인구 이동
while True:
    # 방문 체크
    visited = 0

    # 연합 탐색
    groups = []
    for i in range(N):
        # 시간을 줄이기 위해 짝수 행에서는 짝수 열만, 홀수 행에서는 홀수 행만 탐색 (사방 탐색을 하므로 모두 탐색하게 됨)
        for j in range(i % 2, N, 2):
            # 방문 체크
            if visited & 1 << (N * i + j):
                continue
            visited |= 1 << (N * i + j)

            # 현재 위치에 대한 연합 위치, 연합 인구
            g, p = [(i, j)], A[i][j]

            # 연합의 위치를 담은 큐
            q = deque([(i, j)])
            while q:
                # 현재 위치
                r, c = q.popleft()

                # 사방 탐색
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]

                    # 땅의 범위 및 인구 차이 확인
                    if not (0 <= nr < N and 0 <= nc < N) or not (L <= abs(A[r][c] - A[nr][nc]) <= R):
                        continue

                    # 방문 체크
                    if visited & 1 << (N * nr + nc):
                        continue
                    visited |= 1 << (N * nr + nc)

                    # 다음 위치 큐에 넣기
                    g.append((nr, nc))
                    p += A[nr][nc]
                    q.append((nr, nc))

            # 연합 추가
            if len(g) > 1:
                groups.append((g, p // len(g)))

    # 연합이 없는 경우 끝내기
    if len(groups) == 0:
        break

    # 연합 내 인구 이동
    for g, p in groups:
        for r, c in g:
            A[r][c] = p

    # 일수 증가
    day += 1

print(day)