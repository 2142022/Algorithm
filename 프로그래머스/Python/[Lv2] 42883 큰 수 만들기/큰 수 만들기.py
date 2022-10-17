from collections import deque

def solution(number, k):
    # number의 크기
    N = len(number)
    
    # 제거한 숫자의 개수
    cnt = 0
    
    # 결과
    result = deque()
    
    # 숫자 하나씩 결과에 넣기
    for i in range(N):
        # 집어넣을 값
        num = number[i]
        
        # k개의 수를 모두 삭제했다면 나머지는 모두 집어넣기
        if cnt == k:
            result.append(num)
        
        else:
            # 이미 있는 값이 집어넣을 값보다 작다면 삭제
            # 최대한 큰 숫자가 제일 왼쪽에 와야하기 때문
            while len(result) > 0 and result[-1] < num:
                result.pop()
                cnt += 1
            
                # k개의 수를 제거하면 끝내기
                if cnt == k:
                    break
            
            # 값 집어넣기
            result.append(num)
            
    # 원소의 개수가 N - k보다 큰 경우에는 가장 작은 숫자 pop
    # ex) number = 11119, k = 2인 경우, 앞에서 삭제되는 원소가 없기 때문에 N-k를 초과
    # ex) number = 99991, k = 2인 경우도 마찬가지
    while len(result) > N - k:
        result.remove(min(result))
        
    return ''.join(result)
        
