# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 칠할 영역의 개수
    N = int(input())

    # 빨간색의 위치
    red = [[0] * 10 for _ in range(10)]
    # 파란색의 위치
    blue = [[0] * 10 for _ in range(10)]

    # 칠하는 영역 정보
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if color == 1:
                    red[i][j] = 1
                else:
                    blue[i][j] = 1

    # 보라색 칸 수
    cnt = 0
    for i in range(10):
        for j in range(10):
            if red[i][j] and blue[i][j]:
                cnt += 1

    print(f'#{t} {cnt}')