from collections import defaultdict, deque
import sys

def solution(n, s, a, b, fares):
    # x지점부터 다른 지점까지의 최소 요금 반환
    def getCost(x):
        # x지점부터 다른 지점까지의 최소 요금
        cost = [sys.maxsize] * (n + 1)
        cost[x] = 0
        
        # 탐색 지점과 요금을 담은 큐
        q = deque([(x, 0)])
        while q:
            # 현재 지점, 현재까지의 요금
            i, c = q.popleft()
            
            # 연결된 지점 탐색
            for ni, nc in connect[i]:
                # 기존 요금보다 더 적다면 큐에 추가
                if c + nc < cost[ni]:
                    cost[ni] = c + nc
                    q.append((ni, c + nc))
                    
        return cost
    
    #####################################################
    
    # 각 지점에서 연결된 지점과 비용
    connect = defaultdict(list)
    for x, y, c in fares:
        connect[x].append((y, c))
        connect[y].append((x, c))
        
    # A, B, S로부터의 요금 구하기
    costA = getCost(a)
    costB = getCost(b)
    costS = getCost(s)
    
    # 최소 택시 요금
    result = sys.maxsize
    
    # 중간지점
    for i in range(1, n + 1):
        result = min(result, costA[i] + costB[i] + costS[i])
    
    return result