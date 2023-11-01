def solution(user_id, banned_id):
    # 두 아이디가 일치하는지 체크
    # id1: 실제 아이디
    # id2: *로 가려진 아이디
    def same(id1, id2):
        # 글자 수가 다른 경우
        if len(id1) != len(id2):
            return False
        
        # 한 글자씩 비교
        for i in range(len(id1)):
            # *인 경우 패스
            if id2[i] == '*':
                continue
            
            # 두 글자가 다른 경우
            if id1[i] != id2[i]:
                return False
            
        return True
    
    ########################################################################
    
    # DFS로 제재 아이디 목록으로 가능한 경우의 수 구하기
    # idx: banned_id의 인덱스
    # temp: 제재 아이디 목록에 올라간 사용자 아이디 (비트마스킹)
    def dfs(idx, temp):
        global cnt
        
        # 제재 아이디 목록이 완성된 경우
        if idx == len(banned_id):
            # 새로운 목록인 경우 결과 갱신
            if temp not in result:
                result.append(temp)
                cnt += 1
            return
        
        # 제재 아이디
        bi = banned_id[idx]
        
        # 아이디 목록 중 제재 아이디에 일치하면서, 아직 목록에 없는 경우 탐색
        for i in range(len(user_id)):
            if not (temp & 1 << i) and same(user_id[i], bi):
                dfs(idx + 1, temp | 1 << i)
                
    ########################################################################
    
    global cnt
    
    # 제재 아이디 목록으로 가능한 모든 경우
    result = []
    # 제재 아이디 목록으로 가능한 경우의 수
    cnt = 0
    
    # DFS로 경우의 수 구하기
    dfs(0, 0)
    
    return cnt