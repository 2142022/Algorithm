from collections import defaultdict, deque
import copy
def solution(tickets):
    # tickets 정렬
    # 스택을 사용하면 처음 경로를 마지막에 탐색해야 하므로, 반대로 정렬
    tickets.sort(reverse = True)
    
    # 항공권 딕셔너리 형태로 바꾸기
    ticket = defaultdict(deque)
    for a, b in tickets:
        ticket[a].append(b)
        
    # 경로
    result = []
    
    # 탐색할 공항 (스택 형식)
    airplane = ["ICN"]
    while airplane:
        # 현재 공항
        a = airplane[-1]
        
        # 다음에 갈 수 있는 공항 추가
        if ticket[a]:
            airplane.append(ticket[a].pop())
        # 갈 수 있는 공항이 없는 경우, 경로에 추가
        else:
            result.append(airplane.pop())
    
    # 반대로 반환
    return result[::-1]
    