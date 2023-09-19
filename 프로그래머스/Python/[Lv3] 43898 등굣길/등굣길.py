def solution(m, n, puddles):
    # 나눌 값
    d = 1000000007
    
    # 각 칸에 갈 수 있는 최단 경로의 개수
    # 첫 행과 첫 열에 물에 잠긴 지역이 있을 수 있으므로 시작 지점만 1로 채우기
    cnt = [[0] * (m + 1) for _ in range(n + 1)]
    cnt[1][1] = 1
    
    # 모든 칸 탐색
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 집은 패스
            if i == 1 and j == 1:
                continue
                
            # 물에 잠긴 지역은 0으로 저장
            # 주의 : 좌표가 (열, 행)으로 돼있음
            if [j, i] in puddles:
                cnt[i][j] = 0
            
            # 그 외 칸은 (위에서 내려오는 경우) + (왼쪽에서 오는 경우)
            else:
                cnt[i][j] = (cnt[i - 1][j] + cnt[i][j - 1])
                
    return cnt[-1][-1] % d