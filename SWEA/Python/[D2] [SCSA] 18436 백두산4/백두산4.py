from collections import deque

# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 지도 크기
    N, M = map(int, input().split())

    # 지도 정보
    board = [list(map(int, input().split())) for _ in range(N)]

    # 보물이 가장 멀 때의 거리, 그 때 좌측 상단에 가까운 보물의 위치
    max_dist, R, C = 0, 0, 0

    # 보물 위치의 시작점 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                # 다른 보물과의 거리
                dist = 0

                # 방문 체크
                visited = [[0] * M for _ in range(N)]
                visited[i][j] = 1

                # 탐색 위치와 이동 거리를 담은 큐
                q = deque([(i, j, 0)])
                while q:
                    # 현재 위치, 현재까지의 이동 거리
                    r, c, d = q.popleft()
                    dist = d

                    # 사방 탐색
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if not (0 <= nr < N and 0 <= nc < M):
                            continue

                        if visited[nr][nc] or board[nr][nc] == 0:
                            continue

                        visited[nr][nc] = 1
                        q.append((nr, nc, d + 1))

                # 숨겨진 보물 체크
                if dist > max_dist:
                    max_dist = dist
                    R = i
                    C = j
                elif dist == max_dist and i + j < R + C:
                    R = i
                    C = j

    print(f'#{TC} {R + 1} {C + 1}')

