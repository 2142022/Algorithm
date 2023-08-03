# https://school.programmers.co.kr/learn/courses/30/lessons/43163

# w1에서 w2로 바꿀 수 있는 지 확인
def change(w1, w2):
    # 서로 다른 알파벳의 개수
    diff = 0
    
    # 알파벳 비교
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
            
            if diff > 2:
                break
                
    # 서로 다른 알파벳이 1개인 경우만 true 반환
    if diff == 1:
        return True
    else:
        return False
    
#######################################################

# 최소 변환 횟수 구하기
# w: 현재 단어, c: 현재까지 변환 횟수
def dfs(w, target, words, c):
    global possible, cnt, visit
    
    # 최종 단어가 되면 끝내기
    if w == target:
        possible = 1
        cnt = min(cnt, c)
        return
    
    # 단어들을 확인하면서 cnt 늘리기
    for i in range(len(words)):
        # 이미 쓴 단어라면 패스
        if visit[i] == 1:
            continue
        
        # 단어 바꿀 수 있다면 단어 바꾸기
        if change(w, words[i]):
            visit[i] = 1
            dfs(words[i], target, words, c + 1)
            visit[i] = 0

#######################################################
            
def solution(begin, target, words):
    # target이 words에 없다면 바로 끝내기
    if target not in words:
        return 0
    
    # words의 단어들을 확인했다면 1, 아니면 0
    global visit
    visit = [0] * len(words)
    
    # 단어를 변환할 수 있으면 1, 아니면 0
    global possible
    possible = 0
    
    # 최소 변환 횟수
    global cnt
    cnt = 2147483647

    # DFS를 통해 최소 변환 횟수 구하기
    dfs(begin, target, words, 0)
    
    # 변환할 수 있다면 최소 변환 회수 반환
    if possible:
        return cnt
    else:
        return 0