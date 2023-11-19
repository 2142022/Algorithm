def solution(n, results):
    # i가 j를 이길 때, 순위 차이
    rank = [[0] * (n + 1) for _ in range(n + 1)]
    for i, j in results:
        rank[i][j] = 1
        rank[j][i] = -1
        
    # 플로이드 워셜로 다른 선수와의 순위 차이 갱신하기
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and rank[i][k] == rank[k][j] == 1:
                    rank[i][j] = 1
                    rank[j][i] = rank[k][i] = rank[j][k] = -1
                    
    # 순위를 매길 수 있는 선수의 수
    cnt = 0
                    
    # 순위 차이가 0이 아닌 경우가 n-1인 경우, 모든 선수와의 순위 차이를 알 수 있음을 의미
    for diff in rank:
        if diff.count(0) == 2:
            cnt += 1
    
    return cnt