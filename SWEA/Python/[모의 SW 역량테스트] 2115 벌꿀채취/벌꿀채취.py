from itertools import combinations

# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 벌통 크기, 선택할 수 있는 벌통 수, 꿀 최대 채취 양
    N, M, C = map(int, input().split())

    # 꿀의 양
    board = [list(map(int, input().split())) for _ in range(N)]

    # 각 칸을 시작점으로 했을 때의 수익
    profit = [[0] * (N - M + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            # 최대 C가 되도록 선택했을 때의 최대 수익
            max_p = 0

            # 선택한 개수
            for cnt in range(1, M + 1):
                # 채취할 꿀
                combs = list(combinations(board[i][j:j + M], cnt))

                # 최대 양 C가 넘지 않는 경우 수익 비교
                for honey in combs:
                    if sum(honey) <= C:
                        max_p = max(max_p, sum([i * i for i in honey]))

            # 현재 수익 저장
            profit[i][j] = max_p

    # 2명의 최대 수익
    result = 0
    for i in range(N):
        for j in range(N - M + 1):
            p1 = profit[i][j]

            for r in range(i, N):
                if r == i:
                    for c in range(j + M, N - M + 1):
                        p2 = profit[r][c]
                        result = max(result, p1 + p2)
                else:
                    for c in range(N - M + 1):
                        p2 = profit[r][c]
                        result = max(result, p1 + p2)

    print(f'#{TC} {result}')