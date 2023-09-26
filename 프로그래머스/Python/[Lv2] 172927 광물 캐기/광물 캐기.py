import sys, copy

# 현재 곡괭이로 5개의 광물 캐기
# idx1: 현재 사용할 곡괭이 번호
# idx2: 현재 캘 광물의 시작 번호
# cnt: 현재까지 사용한 곡괭이 개수
# fatigue: 현재까지 쌓인 피로도
# picks: 현재 남은 곡괭이
# minerals: 현재 남은 광물
def mining(idx1, idx2, cnt, fatigue, picks, minerals):
    global picks_cnt, minerals_cnt, info, min_fatigue
    
    # 현재 곡괭이로 광물을 캤을 때의 피로도
    f = 0
    
    # 최대 광물 5개 캐기
    c = 0
    while idx2 < minerals_cnt and c < 5:
        f += info[minerals[idx2]][idx1]
        idx2 += 1
        c += 1
        
        # 최소 피로도보다 큰 경우 끝내기
        if fatigue + f >= min_fatigue:
            return
        
    # 사용한 곡괭이 개수 및 남은 곡괭이 개수 갱신
    cnt += 1
    picks_copy = copy.deepcopy(picks)
    picks_copy[idx1] -= 1
    
    # 모든 곡괭이를 다 사용하거나 모든 광물을 다 캔 경우 끝내기
    if cnt == picks_cnt or idx2 == minerals_cnt:
        min_fatigue = min(min_fatigue, fatigue + f)
        return
        
    # 다음 곡괭이 선택
    for i in range(3):
        if picks_copy[i]:
            mining(i, idx2, cnt, fatigue + f, picks_copy, minerals)
        
##############################################################################    

def solution(picks, minerals):
    global picks_cnt, minerals_cnt, info, min_fatigue
    
    # 전체 곡괭이 개수
    picks_cnt = sum(picks)
    # 전체 광물 개수
    minerals_cnt = len(minerals)
    
    # 광물을 캘 때의 피로도
    info = {"diamond": (1, 5, 25), "iron": (1, 1, 5), "stone": (1, 1, 1)}
    
    # 최소 피로도
    min_fatigue = sys.maxsize
    
    # 곡괭이 하나 선택하기
    for i in range(3):
        if picks[i]:
            mining(i, 0, 0, 0, picks, minerals)
    
    return min_fatigue