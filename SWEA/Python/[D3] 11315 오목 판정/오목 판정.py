# 5개 이상 연속한 부분이 있는지 확인
def exist():
    global N

    # 왼쪽, 위, 왼쪽 상단 대각선, 오른쪽 상단 대각선 탐색
    dr, dc = (0, -1, -1, -1), (-1, 0, -1, 1)

    # 각 위치, 방향별 연속 개수
    cnt = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 돌이 있는 경우
            if board[i][j] == 'o':
                for d in range(4):
                    ni, nj = i + dr[d], j + dc[d]

                    # 판의 범위를 벗어나 경우
                    if not (0 <= ni < N and 0 <= nj < N):
                        cnt[i][j][d] = 1

                    else:
                        cnt[i][j][d] = cnt[ni][nj][d] + 1

                        # 연속한 5개가 된 경우 끝내기
                        if cnt[i][j][d] == 5:
                            return 1

    return 0

#############################################################

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 판의 크기
    N = int(input())

    # 판
    board = [input().rstrip() for _ in range(N)]

    # 5개 이상 연속한 부분 존재 여부 확인
    if exist():
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')