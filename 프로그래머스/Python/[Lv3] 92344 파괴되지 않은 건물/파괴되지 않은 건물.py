def solution(board, skill):
    # 게임 맵 크기 N X M
    N, M = len(board), len(board[0])
    
    # 적군이면 -1, 아군이면 1
    types = {1: -1, 2: 1}
    
    # 최종적으로 더할 값을 누적합으로 구하기
    # 범위 초과를 방지하기 위해 크기는 (N+1) X (M+1)
    plus = [[0] * (M + 1) for _ in range(N + 1)]
    for t, r1, c1, r2, c2, d in skill:
        # 더할 내구도 값
        p = types[t] * d
        
        # (r1, c1)에 p만큼 더하기
        plus[r1][c1] += p
        # 오른쪽으로 누적합을 더할 예정이므로 c2 다음에는 다시 p만큼 빼서 0으로 만들기
        plus[r1][c2 + 1] -= p
        # 아래쪽으로 누적합을 더할 예정이므로 r2 다음에는 다시 p만큼 빼서 0으로 만들기
        plus[r2 + 1][c1] -= p
        # 오른쪽, 아래쪽으로 누적합을 더하면 (r2 + 1, c2 + 1)에는 -p가 더해지므로 p 더해서 0으로 만들기
        plus[r2 + 1][c2 + 1] += p
        
    # 오른쪽으로 누적합 구하기
    for i in range(N):
        for j in range(1, M):
            plus[i][j] += plus[i][j - 1]
            
    # 아래쪽으로 누적합 구하기
    for i in range(1, N):
        for j in range(M):
            plus[i][j] += plus[i - 1][j]
    
    # 파괴되지 않은 건물 개수
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + plus[i][j] > 0:
                cnt += 1

    return cnt