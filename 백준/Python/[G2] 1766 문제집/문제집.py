import sys
input = sys.stdin.readline

# N: 문제의 수, M: 먼저 푸는 것이 좋은 문제에 대한 정보의 개수
N, M = map(int, input().split())

# 각 문제의 진입차수(노드에 들어오는 간선의 수)
# 먼저 푸는 것이 좋은 문제의 수
indegree = [0] * (N + 1)

# 먼저 푸는 것이 좋은 문제에 대한 정보
info = [[] for i in range(N + 1)]
for i in range(M):
    # A번 문제는 B번 문제보다 먼저 풀기
    A, B = map(int, input().split())
    info[A].append(B)
    indegree[B] += 1

########################### 위상 정렬 ##############################
# 결과: 문제 순서
result = []

# 방문 체크
visit = [0] * (N + 1)

# 모든 문제를 다 뽑을 때까지 반복
for i in range(N):
    # 문제를 뽑았는지 체크(하나를 뽑으면 다시 진입차수를 체크해야 함)
    flag = 0
    
    # 진입차수가 0인 문제 중 난이도가 쉬운(즉, 앞 번호) 문제 뽑기
    for j in range(1, N + 1):
        # 이미 뽑은 문제는 pass
        if indegree[j] == 0 and visit[j] == 0:
            result.append(j)
            visit[j] = 1
            flag = 1

            # j번째 다음으로 풀 수 있는 문제들의 진입차수 낮추기
            for k in info[j]:
                indegree[k] -= 1

        if flag == 1:
            break

###################################################################
# 출력
for i in result:
    print(i, end = ' ')
