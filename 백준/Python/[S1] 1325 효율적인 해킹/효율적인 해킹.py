from collections import deque
import sys
input = sys.stdin.readline

# num번 컴퓨터를 해킹했을 때 총 해킹할 수 있는 컴퓨터의 개수 반환
def bfs(num):
    queue = deque([num])

    # i번 컴퓨터가 해킹되면 hacking[i] = 1
    global N
    hacking = [0] * (N + 1)
    hacking[num] = 1

    # 해킹 횟수
    hc = 0

    # queue의 원소가 없어질 때까지 반복
    while queue:
        #queue의 첫 원소 pop
        num = queue.popleft()
        hc += 1

        # num과 신뢰 관계에 있는 컴퓨터가 있을 때
        if trust[num] != []:
            for i in trust[num]:
                # 그 컴퓨터가 아직 해킹되지 않았을 때
                if hacking[i] == 0:
                    queue.append(i)
                    hacking[i] = 1

    # 총 해킹 횟수 반환
    return hc


# 1 ~ N번까지의 컴퓨터
# M: 신뢰 관계의 개수
N, M = map(int, input().split())

# 신뢰 관계 입력받기
trust = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    trust[b] += [a]

# 1 ~ N번까지의 컴퓨터를 해킹했을 때 해킹할 수 있는 컴퓨터의 개수
cnt = [0] * (N + 1)

# BFS로 계산하기
cnt_max = 0
for i in range(1, N + 1):
    cnt[i] = bfs(i)
    if cnt[i] > cnt_max:
        cnt_max = cnt[i]

# cnt[i]의 max값과 일치하는 인덱스(i)
for i in range(1, N + 1):
    if cnt[i] == cnt_max:
        print(i, end = ' ')
