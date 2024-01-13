from heapq import heappush, heappop

def solution(n, m, x, y, r, c, k):
    # k - (출발지와 목적지 사이의 거리)가 짝수가 아니면 탈출 불가
    # k보다 작은 거리로 도착하면 이동 후에 목적지까지 돌아오기까지 2번이 걸리기 때문
    total = abs(x - r) + abs(y - c)
    if total > k or (k - total) % 2:
        return 'impossible'
    
    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
    ch = ('u', 'd', 'l', 'r')
    
    # 이동 경로, 현재 위치를 담은 최소 힙
    h = []
    heappush(h, ('', x, y))
    while h:
        # 이동 경로, 현재 위치
        p, i, j = heappop(h)
        
        # 현재까지의 이동 거리
        l = len(p)
        
        # 탈출한 경우 경로 반환
        if i == r and j == c and l == k:
            return p
            
        # 사방 탐색
        for d in range(4):
            # 다음 위치
            ni, nj = i + dr[d], j + dc[d]
            
            # 범위를 벗어난 경우 패스
            if not (1 <= ni <= n and 1 <= nj <= m):
                continue
                
            # 도착 지점까지 k 이내로 갈 수 없는 경우 패스
            if abs(ni - r) + abs(nj - c) + l + 1 > k:
                continue
                
            # 다음 위치 힙에 넣기
            heappush(h, (p + ch[d], ni, nj))
