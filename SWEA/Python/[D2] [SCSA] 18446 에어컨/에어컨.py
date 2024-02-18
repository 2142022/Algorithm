# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 지도 크기, 필터 개수, 종류
    N, M, K, T = map(int, input().split())

    # 쾌적하지 않은 영역의 개수
    cnt = N * M

    # 각 영역에 있는 필터 체크
    board = [[[0] * (T + 1) for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        # 필터 종류, 시작 위치, 필터 크기
        t, si, sj, h, w = map(int, input().split())

        # 필터 행
        for r in range(si, si + h):
            if not (0 <= r < N):
                break

            # 필터 열
            for c in range(sj, sj + w):
                if not (0 <= c < M):
                    break

                # 이미 존재하는 필터인 경우 패스
                if board[r][c][t]:
                    continue

                # 필터 체크 및 쾌적한 영역 체크
                board[r][c][t] = 1
                if sum(board[r][c]) == (T + 1):
                    cnt -= 1

    # 쾌적하지 않은 영역 개수
    print(f'#{TC} {cnt}')