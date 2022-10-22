# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    # 참가자와 완주자를 이름순으로 정렬
    participant.sort()
    completion.sort()
    
    # 참가자와 완주자의 이름을 하나씩 비교
    for i in range(len(completion)):
        
        # 이름이 다르다면 완주하지 못한 선수
        if participant[i] != completion[i]:
            return participant[i]
    
    # 끝까지 비교했는데 이름이 다른 사람이 없다면 마지막 남은 참가자가 완주하지 못한 선수
    return participant[-1]
