from collections import deque

def solution(maps):
    # maps 크기
    n, m = len(maps), len(maps[0])

    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
    
    # 방문 체크
    visited = 0
    
    # 지나간 칸 개수, 현재 위치를 담은 큐
    q = deque([(1, 0, 0)])
    while q:
        # 지나간 칸 개수, 현재 위치
        cnt, r, c = q.popleft()
        
        # 도착한 경우 끝내기
        if r == n - 1 and c == m - 1:
            return cnt
        
        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            
            # 범위를 벗어난 경우 패스
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            
            # 벽인 경우 패스
            if maps[nr][nc] == 0:
                continue
                
            # 방문 체크
            if visited & 1 << (m * nr + nc):
                continue
            visited |= 1 << (m * nr + nc)

            # 다음 위치 큐에 넣기
            q.append((cnt + 1, nr, nc))
        
    # 도착할 수 없는 경우 -1 리턴
    return -1