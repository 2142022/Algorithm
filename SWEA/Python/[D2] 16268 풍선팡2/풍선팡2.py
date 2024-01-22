# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 격자판 크기
    N, M = map(int, input().split())

    # 풍선 정보
    A = [list(map(int, input().split())) for _ in range(N)]

    # 사방 탐색용
    di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 날릴 수 있는 최대 꽃가루 수
    mx = 0

    # 한 칸씩 탐색
    for i in range(N):
        for j in range(M):
            # 총 꽃가루 수
            total = A[i][j]

            # 사방 탐색
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < M:
                    total += A[ni][nj]

            # 최대 꽃가루 수 비교
            mx = max(mx, total)

    print(f'#{t} {mx}')