from collections import deque

# 테스트 케이스 개수
T = int(input())
for tc in range(1, T + 1):
    # 지도 크기
    N, M = map(int, input().split())

    # 분출 위치
    sr, sc = map(int, input().split())

    # 분출하지 않은 화산지대 면적
    area = 0

    # 지도 (1: 분출 시작점, 0: 화산지대, -1: 암석지대)
    board = []
    for _ in range(N):
        row = list(map(lambda x: int(x) - 1, input().split()))
        board.append(row)
        area += row.count(0)

    # 분출 시작점이 암석지대인 경우
    if board[sr][sc] == -1:
        print(f'#{tc} {0} {area}')
        continue
    board[sr][sc] = 1
    area -= 1

    # 분출 완료 시간
    time = 1

    # 탐색 위치를 담은 큐
    q = deque([(sr, sc)])
    while q:
        # 현재 위치
        r, c = q.popleft()

        # 분출 시간
        t = board[r][c]
        time = t

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
                board[nr][nc] = t + 1
                area -= 1
                q.append((nr, nc))

    print(f'#{tc} {time} {area}')



