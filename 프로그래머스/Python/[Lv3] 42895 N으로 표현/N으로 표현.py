def solution(N, number):
    # N이 number인 경우 바로 1 반환
    if N == number:
        return 1
    
    # N을 cnt개 사용하는 경우
    # = N*cnt
    #   + (N을 1개 사용하는 경우) (사칙 연산) (N을 cnt-1개 사용하는 경우)
    #   + (N을 2개 사용하는 경우) (사칙 연산) (N을 cnt-2개 사용하는 경우)
    #   + ...
    #   + (N을 cnt-1개 사용하는 경우) (사칙 연산) (N을 1개 사용하는 경우)
    
    # number를 만들 수 있는 N의 최소 개수
    answer = -1
    
    # N을 i개 사용해서 만들 수 있는 수
    nums = [set() for _ in range(9)]
    nums[1].add(N)
    
    # N을 i번 사용
    for i in range(2, 9):
        # N을 연속으로 i번 사용한 수 추가
        nums[i].add(int(str(N) * i))
        
        # nums[j]와 nums[i - j]의 원소들을 사칙연산하기
        for j in range(1, i):
            for n1 in nums[j]:
                for n2 in nums[i - j]:
                    nums[i].add(n1 + n2)
                    nums[i].add(n1 - n2)
                    nums[i].add(n1 * n2)
                    if n2 > 0:
                        nums[i].add(n1 / n2)
                        
        # number가 있는지 확인
        if number in nums[i]:
            answer = i
            break
            
    return answer
