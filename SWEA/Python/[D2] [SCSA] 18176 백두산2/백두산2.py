from collections import deque

# BFS로 최소 대피 시간 구하기
def bfs(N, M):
    while q:
        # 마그마 혹은 사람 번호(3/4), 마그마 혹은 사람의 위치, 이동 시간
        p, r, c, t = q.popleft()

        # 현재 사람인데 이미 마그마가 덮친 경우 패스
        if p == 4 and board[r][c] == 3:
            continue

        # 사방 탐색
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            # 다음 위치
            nr, nc = r + dr, c + dc

            # 범위 확인
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 암석지대인 곳은 마그마, 사람 모두 이동 불가능
            if board[nr][nc] == 0:
                continue

            # 마그마인 경우
            if p == 3:
                # 이미 방문한 곳이나 대피소는 패스
                if board[nr][nc] in (2, 3):
                    continue
                board[nr][nc] = 3
                q.append((3, nr, nc, t + 1))

            # 사람인 경우
            else:
                # 이미 방문한 곳이나 마그마가 있는 경우
                if board[nr][nc] in (3, 4):
                    continue

                # 대피소인 경우 끝내기
                elif board[nr][nc] == 2:
                    return t + 1

                board[nr][nc] = 4
                q.append((4, nr, nc, t + 1))

    # 대피 불가
    return -1

################################################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 구역 크기
    N, M = map(int, input().split())

    # 구역
    board = []
    # 마그마/사람 번호(3/4), 마그마 혹은 사람의 위치, 이동 시간을 담은 큐
    q = deque()
    # 사람의 시작 위치
    sr = sc = 0
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j, num in enumerate(row):
            if num == 3:
                q.append((3, i, j, 0))
            elif num == 4:
                sr, sc = i, j
    # 마지막에 사람의 위치를 큐의 맨 앞에 넣기
    q.appendleft((4, sr, sc, 0))

    # BFS로 최소 대피 시간 구하기
    print(f'#{t} {bfs(N, M)}')