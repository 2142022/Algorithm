from collections import deque

def solution(priorities, location):
    # 대기 큐 생성
    q = deque(priorities)

    # 원하는 프로세스의 실행 순서
    cnt = 1

    # 대기중인 프로세스 하나씩 꺼내기
    while q:
        # 현재 프로세스의 우선 순위
        order = q.popleft()

        # 가장 높은 우선 순위인 경우 프로세스 실행
        if not q or order >= max(q):
            # 원하는 프로세스인 경우, 순서 리턴
            if location == 0:
                return cnt

            # 원하는 프로세스가 아닌 경우, 위치 변경
            else:
                location -= 1
                cnt += 1

        # 가장 높은 우선 순위가 아닌 경우 다시 큐에 넣기
        else:
            q.append(order)

            # 원하는 프로세스의 위치 변경
            if location == 0:
                location = len(q) - 1
            else:
                location -= 1
    