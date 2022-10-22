# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    # 유저의 수
    N = len(id_list)
    
    # report[i][j]: i번째 사람이 j번째 사람을 신고
    info = [[0] * N for i in range(N)]
    
    # 신고 정보 입력받기
    for i in report:
        # user: 신고한 유저, warn: 신고 당한 유저
        user, warn = map(str, i.split())
        
        info[id_list.index(user)][id_list.index(warn)] = 1
        
    # 각 유저가 받는 메일 수
    answer = [0] * N
        
    # k번 이상 신고 당한 유저 구하기
    for j in range(N):
        # j번째 사람이 신고당한 횟수
        cnt = 0
        
        # j번째 사람을 신고한 유저
        mail = [0] * N
        
        # j번째 사람을 신고한 사람은 메일 1개 증가시키기
        for i in range(N):
            if info[i][j] == 1:
                cnt += 1
                mail[i] += 1
        
        # 신고당한 횟수가 k개 이상이라면 유저의 메일 개수 증가시키기
        if cnt >= k:
            answer = [answer[i] + mail[i] for i in range(N)]
    
    return answer
