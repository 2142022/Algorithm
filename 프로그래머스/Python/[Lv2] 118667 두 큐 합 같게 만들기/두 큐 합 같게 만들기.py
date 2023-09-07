from collections import deque

def solution(queue1, queue2):
    # 큐를 deque로 형태로 만든 것
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 각 큐의 합
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    # 두 큐의 합이 홀수라면 반으로 나눌 수 없으므로 끝내기
    if (sum1 + sum2) % 2:
        return -1
    
    # 연산 횟수
    cnt = 0
    # 무한 반복하지 않도록 제한하기
    limit = len(q1) * 2
    
    while limit:
        # 큐1의 합이 더 크다면 큐1의 원소를 큐2에 넣기
        while sum1 > sum2:
            num = q1.popleft()
            sum1 -= num
            sum2 += num
            q2.append(num)
            cnt += 1
            
        # 큐2의 합이 더 크다면 큐2의 원소를 큐1에 넣기
        while sum2 > sum1:
            num = q2.popleft()
            sum1 += num
            sum2 -= num
            q1.append(num)
            cnt += 1
            
        # 두 큐의 합이 동일하다면 끝내기
        if sum1 == sum2:
            return cnt
        
        limit -= 1
        
    # 두 큐의 원소 합을 같게 만들 수 없는 경우 -1 반환
    return -1