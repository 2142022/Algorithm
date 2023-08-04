from itertools import combinations

# 테스트케이스 개수
T = int(input())

# T개의 테스트케이스
for t in range(1, T + 1):
    # 식재료 수
    N = int(input())

    # 식재료들의 시너지
    S = [list(map(int, input().split())) for _ in range(N)]

    # A와 B의 시너지의 최소 차이
    diff = 2147483647

    # A의 재료로 N/2개 뽑기
    for A in combinations([i for i in range(N)], N // 2):
        # A의 시너지
        SA = 0
        # B의 시너지
        SB = 0

        # A와 B의 시너지의 구하기
        for i in range(N):
            for j in range(N):
                # A의 재료인 경우
                if i in A and j in A:
                    SA += S[i][j]
                # B의 재료인 경우
                elif i not in A and j not in A:
                    SB += S[i][j]

        diff = min(diff, abs(SA - SB))

    print("#%d %d"%(t, diff))