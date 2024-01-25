# 테스트케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 퍼즐 크기, 단어 길이
    N, K = map(int, input().split())

    # 퍼즐
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]

    # 길이가 K인 단어 개수
    cnt = 0

    # 행 / 열
    for i in range(N + 1):
        # 가로 단어 길이, 세로 단어 길이
        w = h = 0

        # 열 / 행
        for j in range(N + 1):
            # 가로 단어 길이 갱신
            num = puzzle[i][j]
            if num == 0:
                if w == K:
                    cnt += 1
                w = 0
            else:
                w += 1

            # 세로 단어 길이 갱신
            num = puzzle[j][i]
            if num == 0:
                if h == K:
                    cnt += 1
                h = 0
            else:
                h += 1

    print(f'#{t} {cnt}')