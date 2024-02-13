from collections import deque

# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 지도 크기
    N = int(input())

    # 지도
    board = [list(map(int, input())) for _ in range(N)]

    # 각 위치까지의 최소 복구 작업 시간
    time = [[9 * N * N] * N for _ in range(N)]
    time[0][0] = 0

    # 탐색 위치와 현재까지의 복구 작업 시간을 담은 큐
    q = deque([(0, 0, 0)])
    while q:
        # 탐색 위치와 현재까지의 복구 작업 시간
        r, c, t = q.popleft()

        # 도착 지점에 도착한 경우 끝내기
        if r == N - 1 and c == N - 1:
            time[r][c] = min(time[r][c], t)
            continue

        # 현재 위치에서의 최소 복구 작업 시간보다 오래 걸리는 경로는 패스
        if t != time[r][c]:
            continue

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < N and 0 <= nc < N and time[nr][nc] > t + board[nr][nc]:
                time[nr][nc] = t + board[nr][nc]
                q.append((nr, nc, t + board[nr][nc]))

    print(f'#{T} {time[-1][-1]}')