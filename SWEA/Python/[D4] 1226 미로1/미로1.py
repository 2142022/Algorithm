from collections import deque

# 미로 크기
N = 16

# 테스트 케이스
for _ in range(10):
    # 테스트 케이스 번호
    t = int(input())

    # 출발지, 도착지
    si = sj = di = dj = -1

    # 미로
    maze = []
    for i in range(N):
        info = list(map(int, input()))
        maze.append(info)
        for j in range(N):
            if info[j] == 2:
                si, sj = i, j
            elif info[j] == 3:
                di, dj = i, j

    # 도착지 도달 가능 여부
    possible = 0

    # 방문 체크
    visited = 1 << (N * si + sj)

    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 현재 위치를 담은 큐
    q = deque([(si, sj)])
    while q:
        # 현재 위치
        r, c = q.popleft()

        # 도착지에 도착한 경우 끝내기
        if r == di and c == dj:
            possible = 1
            break

        # 사방 탐색
        for d in range(4):
            # 다음 위치
            nr, nc = r + dr[d], c + dc[d]

            # 범위를 벗어난 경우 패스
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 방문 체크
            if visited & 1 << (N * nr + nc):
                continue
            visited |= 1 << (N * nr + nc)

            # 벽이 아닌 경우, 다음 위치 큐에 넣기
            if maze[nr][nc] != 1:
                q.append((nr, nc))

    print(f'#{t} {possible}')