# 테스트케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 보드 크기
    N, M = map(int, input().split())

    # 꽃가루 개수
    board = [list(map(int, input().split())) for _ in range(N)]

    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 날릴 수 있는 최대 꽃가루 수
    mx_cnt = 0

    # 중간 풍선의 위치
    for i in range(N):
        for j in range(M):
            # 현재 위치에서 터트릴 수 있는 꽃가루, 현재 위치의 꽃가루 개수
            cnt = limit = board[i][j]

            # 사방 탐색
            for d in range(4):
                ni, nj = i, j
                for k in range(limit):
                    ni += dr[d]
                    nj += dc[d]
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += board[ni][nj]

            # 최대 꽃가루 수 비교
            mx_cnt = max(mx_cnt, cnt)

    print(f'#{t} {mx_cnt}')