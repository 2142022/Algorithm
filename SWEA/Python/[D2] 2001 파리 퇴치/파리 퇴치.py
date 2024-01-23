# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 배열 크기, 파리채 크기
    N, M = map(int, input().split())

    # 배열 (누적합으로 저장)
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(1, N):
            board[i][j] += board[i][j - 1]
    for j in range(N):
        for i in range(1, N):
            board[i][j] += board[i - 1][j]

    # 최대한 많은 파리를 죽였을 때의 개수
    cnt = 0

    # 파리채의 오른쪽 하단 부분 기준 탐색
    for i in range(M - 1, N):
        for j in range(M - 1, N):
            # 현재 위치에서 죽이는 파리 개수
            num = board[i][j]
            if i >= M:
                num -= board[i - M][j]
            if j >= M:
                num -= board[i][j - M]
            if i >= M and j >= M:
                num += board[i - M][j - M]

            cnt = max(cnt, num)

    print(f'#{t} {cnt}')