from collections import deque
import sys
input = sys.stdin.readline

# A를 B로 만드는데 필요한 최소 연산 횟수 구하기
def bfs(a, b):
    # 이미 한 번 만들어 본 수
    visited = {a}

    # 탐색할 수, 현재까지의 연산 횟수를 담은 큐
    q = deque([(a, 1)])
    while q:
        # 탐색할 수, 현재까지의 연산 횟수
        num, cnt = q.popleft()

        # X2
        nn = num * 2
        # B가 만들어진 경우 끝내기
        if nn == B:
            return cnt + 1
        if nn <= 1000000000 and nn not in visited:
            visited.add(nn)
            q.append((nn, cnt + 1))

        # 오른쪽에 1 추가
        nn = num * 10 + 1
        # B가 만들어진 경우 끝내기
        if nn == B:
            return cnt + 1
        if nn <= 1000000000 and nn not in visited:
            visited.add(nn)
            q.append((nn, cnt + 1))

    # B를 만들 수 없는 경우
    return -1

##########################################################

# 두 정수
A, B = map(int, input().split())

# A를 B로 만드는데 필요한 최소 연산 횟수
print(bfs(A, B))