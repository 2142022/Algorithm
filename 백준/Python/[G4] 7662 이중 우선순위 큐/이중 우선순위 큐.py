import heapq
import sys
input = sys.stdin.readline

# 테스트케이스 개수
T = int(input())

# T개의 테스트케이스
for t in range(T):
    # 연산의 개수
    K = int(input())

    # 최대 힙
    maxQ = []

    # 최소 힙
    minQ = []

    # 방문 체크
    visit = [0] * K

    # K개의 연산
    for k in range(K):
        op, n = map(str, input().split())

        # I: 최대 힙과 최소 힙에 (n, k) 삽입
        # 최대 힙은 -(마이너스) 붙여서 넣
        if op == 'I':
            heapq.heappush(maxQ, (int(n) * (-1), k))
            heapq.heappush(minQ, (int(n), k))

        # D 1: 최대값 삭제
        elif op == 'D' and n == '1':
            # 최소 힙에서 이미 삭제했다면 계속 뽑기
            while len(maxQ) > 0 and visit[maxQ[0][1]] == 1:
                heapq.heappop(maxQ)
                
            # 최대 힙에서 최대값 삭제
            if len(maxQ) > 0:
                visit[maxQ[0][1]] = 1
                heapq.heappop(maxQ)

        # D -1: 최솟값 삭제
        elif op == 'D' and n == '-1':
            # 최대 힙에서 이미 삭제했다면 계속 뽑기
            while len(minQ) > 0 and visit[minQ[0][1]] == 1:
                heapq.heappop(minQ)
                
            # 최소 힙에서 최솟값 삭제
            if len(minQ) > 0:
                visit[minQ[0][1]] = 1
                heapq.heappop(minQ)

    # 최소 힙과 최대 힙에서 서로 삭제한 원소 뽑기
    while len(maxQ) > 0 and visit[maxQ[0][1]] == 1:
        heapq.heappop(maxQ)
    while len(minQ) > 0 and visit[minQ[0][1]] == 1:
        heapq.heappop(minQ)

    # 최소 힙과 최대 힙이 비어있다면 'EMPTY' 출력
    if len(minQ) == 0 and len(maxQ) == 0:
        print('EMPTY')
    else:
        print((-1) * maxQ[0][0], minQ[0][0])
