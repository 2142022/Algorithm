# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# k: 현재 남은 피로도
# idx: 현재 탐험할 던전
# cnt: 현재까지 탐험한 던전 수
def dfs(k, dungeons, idx, cnt):
    global max_cnt
    global N
    
    # 모든 던전을 탐험하면 끝내기
    if idx == N:
        max_cnt = max(cnt, max_cnt)
        return

    # 현재 피로도로 던전을 탐험할 수 있는 경우에만 탐험
    if k >= dungeons[idx][0]:
        # 현재 던전을 탐험
        dfs(k - dungeons[idx][1], dungeons, idx + 1, cnt + 1)
    
    # 현재 던전을 탐험하지 않는 경우
    dfs(k, dungeons, idx + 1, cnt)

#####################################################################

def solution(k, dungeons):
    # 유저가 탐험한 최대 던전 수
    global max_cnt
    max_cnt = 0
    
    # 던전 수
    global N
    N = len(dungeons)

    # 던전을 (최소 필요 피로도 - 소모 피로도) 순으로 내림차순 정렬
    # (최소 필요 피로도 - 소모 피로도)가 크다는 것은
    # 최소 필요 피로도가 높으면서 소모 피로도가 낮다는 뜻
    # 즉, 다른 던전을 탐험할 기회가 많아짐
    dungeons.sort(key = lambda x : x[0]-x[1], reverse = True)

    dfs(k, dungeons, 0, 0)
    
    return max_cnt
