from collections import deque

# 탈주범이 위치할 수 있는 장소의 개수 구하기
def find():
    # 방문 체크 (도착 시간 저장)
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1

    # 탈주범이 위치할 수 있는 장소의 개수
    cnt = 1

    # 탐색 위치를 담은 큐
    q = deque([(R, C)])
    while q:
        # 현재 위치와 이동 시간
        r, c = q.popleft()
        t = visited[r][c]

        # 더 이동 가능한 경우 이동
        if t + 1 > L:
            break

        # 현재 위치에서 갈 수 있는 방향 탐색
        for d in D[board[r][c]]:
            nr, nc = r + dr[d], c + dc[d]

            # 범위 & 방문 체크
            if not (0 <= nr < N and 0 <= nc < M) or visited[nr][nc]:
                continue

            # 현재 터널과 이어진 경우 이동 가능
            if not board[nr][nc] or (d + 2) % 4 not in D[board[nr][nc]]:
                continue

            # 이동
            visited[nr][nc] = t + 1
            cnt += 1
            q.append((nr, nc))

    return cnt

####################################################################################################

# 터널 구조물별 이동 가능한 방향
D = {1: (0, 1, 2, 3), 2: (0, 2), 3: (1, 3), 4: (0, 1), 5: (1, 2), 6: (2, 3), 7: (3, 0)}

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 지도 크기, 맨홀 뚜껑 위치, 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())

    # 지도
    board = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{TC} {find()}')