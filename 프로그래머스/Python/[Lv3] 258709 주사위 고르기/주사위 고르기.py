from itertools import combinations
from collections import defaultdict

def solution(dice):
    # A와 B가 뽑은 주사위들의 합의 개수 구하기
    # idx: 주사위 묶음에서의 인덱스
    # A, B: 현재까지의 A, B 주사위의 합
    def get_sum(idx, A, B, m):
        # 모든 주사위를 탐색한 경우
        if idx == m:
            sumA[A] += 1
            sumB[B] += 1
            return
        
        # 현재 주사위 면 선택
        for i in range(6):
            get_sum(idx + 1, A + dice[diceA[idx]][i], B + dice[diceB[idx]][i], m)
            
    ######################################################################################
    
    # 주사위 개수
    n = len(dice)
    
    # A가 뽑을 주사위 개수
    m = n // 2
    
    # 주사위 번호가 1부터 시작하므로 맨 앞에 빈 리스트 추가
    dice.insert(0, [])
    
    # 뽑은 주사위 묶음별 승리 횟수
    win = defaultdict(int)
    
    # 선택한 주사위 묶음 체크
    check = set()
    
    # 주사위 뽑기
    for select in combinations(range(1, n + 1), m):
        # A, B의 주사위 묶음
        diceA, diceB = list(select), [d for d in range(1, n + 1) if d not in select]
        
        # 이미 확인한 주사위 묶음 체크
        if tuple(diceA) in check:
            continue
        check.add(tuple(diceB))
        
        # A, B가 뽑은 주사위들의 합의 개수
        sumA = defaultdict(int)
        sumB = defaultdict(int)
        get_sum(0, 0, 0, m)
        
        # 승패 정하기
        for a in sumA:
            for b in sumB:
                # 현재 경우의 수
                cnt = sumA[a] * sumB[b]
                if a > b:
                    win[tuple(diceA)] += cnt
                elif b > a:
                    win[tuple(diceB)] += cnt
                    
    return max(win, key = win.get)