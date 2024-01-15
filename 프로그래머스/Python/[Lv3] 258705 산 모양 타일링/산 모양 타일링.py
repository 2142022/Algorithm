def solution(n, tops):
    # 나눌 수
    M = 10007
    
    # 사다리꼴에 있는 정삼각형의 개수
    N = 2 * n + 1
    
    # 사다리꼴에 있는 각 정삼각형까지 만들 수 있는 경우의 수
    dp = [0] * N
    dp[0] = 1
    dp[1] = 3 if tops[0] else 2
    for i in range(2, N):
        # 이전 사다리꼴까지의 경우의 수, 두 번째 전 사다리꼴까지의 경우의 수
        a, b = dp[i - 1], dp[i - 2]
        
        # 이전 사다리꼴에서 정삼각형을 붙이거나, 두 번째 전 사다리꼴에서 마름모를 붙이기
        c = (a + b) % M
        dp[i] = c
        
        # 현재 위치 위에 정삼각형이 있는 경우, 정삼각형을 올리거나 이전 사다리꼴에서 마름모 붙이기
        d, m = divmod(i, 2)
        if m and tops[d]:
            dp[i] = (c + a) % M
    
    return dp[-1]