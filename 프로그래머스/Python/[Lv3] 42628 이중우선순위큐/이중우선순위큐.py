def solution(operations):
    # 이중 우선순위 큐
    q = []
    for op in operations:
        # 명령어와 숫자
        s, n = op[0], int(op[2:])
        
        # 숫자 삽입
        if s == "I":
            q.append(n)

        # 숫자 삭제
        elif q:
            # 최댓값 삭제
            if n == 1:
                q.remove(max(q))

            # 최솟값 삭제
            else:
                q.remove(min(q))
    
    # 큐의 최댓값, 최솟값 반환
    if q:
        return [max(q), min(q)]
    else:
        return [0, 0]