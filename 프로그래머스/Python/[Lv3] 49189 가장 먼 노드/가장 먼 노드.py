from collections import deque

def solution(n, edge):
    # 각 노드와 연결된 노드
    connect = [[] for _ in range(n + 1)]
    for a, b in edge:
        connect[a].append(b)
        connect[b].append(a)
        
    # 가장 멀리 떨어진 노드까지의 거리
    md = -1
    # 가장 멀리 떨어진 노드의 개수
    cnt = 0
    
    # 방문 체크용
    visited = [0] * (n + 1)
    
    # 현재 노드와 노드 1로부터의 거리를 담은 큐
    q = deque()
    q.append((1, 0))
    
    # 큐가 빌 때까지 반복
    while q:
        # 현재 노드와 노드 1로부터의 거리
        node, d = q.popleft()
        
        # 이미 방문한 곳은 패스
        if visited[node]:
            continue
        
        # 방문 체크
        visited[node] = 1
        
        # 가장 먼 거리와 같다면 개수 추가
        if d == md:
            cnt += 1
        # 가장 먼 거리보다 크다면 갱신
        elif d > md:
            md = d
            cnt = 1
        
        # 현재 노드와 연결된 노드 큐에 추가
        for i in connect[node]:
            # 이미 방문한 곳은 패스
            if visited[i]:
                continue
            
            # 큐에 추가
            q.append((i, d + 1))
            
    return cnt