from itertools import permutations

def solution(n, weak, dist):
    # 취약점이 1개인 경우 1 반환
    if len(weak) == 1:
        return 1
    
    # 취약 지점 개수
    lw = len(weak)
    # 친구 수
    ld = len(dist)

    # 원형인 외벽을 선형으로 바꾸기 위해 weak를 2배로 늘리기
    weak += [n + i for i in weak]
    # 거리가 먼 순서대로 정렬
    dist.sort(reverse = True)

    # 투입할 친구 수
    for fcnt in range(1, ld + 1):
        # 가장 멀리 탐색할 수 있는 fcnt명의 친구들의 자리 바꾸기
        for friends in permutations(dist[:fcnt], fcnt):
            # 첫 투입 지점
            for i in range(lw):
                # friends, 취약 지점의 인덱스
                fidx = 0
                widx = i
                
                # 모든 취약 지점을 탐색하거나 모든 친구들이 투입된 경우 끝내기
                while widx - i != lw and fidx != fcnt:
                    # 현재 위치
                    now = weak[widx]
                    
                    # 현재 투입된 친구가 갈 수 있는 최대 위치
                    pos = now + friends[fidx]
                    
                    # 지나온 취약 지점만큼 인덱스 증가
                    while weak[widx] <= pos:
                        widx += 1
                        
                    # 다음 친구의 인덱스
                    fidx +=1
                    
                # 모든 취약 지점을 탐색한 경우 끝내기
                if widx - i == lw:
                    return fcnt
                
    # 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우 
    return -1