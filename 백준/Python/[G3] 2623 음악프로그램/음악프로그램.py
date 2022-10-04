import sys
input = sys.stdin.readline
from collections import deque

# N: 가수의 수, M: 보조 PD의 수
N, M = map(int, input().split())

# 각 가수의 진입차수
indegree = [0] * (N + 1)

# 출연 순서 정보
info = [[] for i in range(N + 1)]
for i in range(M):
    tmp = list(map(int, input().split()))

    for j in range(1, tmp[0]):
        info[tmp[j]].append(tmp[j + 1])
        indegree[tmp[j + 1]] += 1

############################## 위상 정렬 #################################
# 결과: 가수 순서
result = []

q = deque()

# 진입차수가 0인 가수 넣기
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

# 큐의 원소가 없어질 때까지 반복
while q:
    now = q.popleft()
    result.append(now)

    # 현재 가수 다음에 올 수 있는 가수의 진입차수 낮추기
    for i in info[now]:
        indegree[i] -= 1

        # 만약 진입차수가 0이라면 큐에 추가
        if indegree[i] == 0:
            q.append(i)

##########################################################################
# 가수가 N명이 아니라 순서 정하기 불가능
if len(result) != N:
    print(0)
else:
    for i in result:
        print(i)
