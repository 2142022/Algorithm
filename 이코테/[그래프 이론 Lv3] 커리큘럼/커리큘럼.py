from collections import deque
import sys
input = sys.stdin.readline

# 강의의 수
N = int(input())

# 연결 리스트 (사전에 들어야 하는 강의 번호)
graph = [[] for _ in range(N + 1)]

# 각 강의 시간
time = [0] * (N + 1)

# 각 강의를 수강하기까지 걸리는 최소 시간
# time과 함께 초기화
result = [0] * (N + 1)

# 각 강의를 수강하기 전에 필수로 수강해야 하는 강의의 개수
need = [0] * (N + 1)

# 각 강의의 시간과 사전 강의 정보 입력받기
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    need[i] = len(temp) - 2
    time[i] = result[i] = temp[0]
    for j in range(1, need[i] + 1):
        graph[temp[j]].append(i)

# 사전 강의 개수가 0이 된 강의들의 목록 (진입차수가 0인 노드)
q = deque()

# 진입차수가 0인 노드를 큐에 넣기
for i in range(1, N + 1):
    if need[i] == 0:
        q.append(i)

# 큐가 빌 때까지 반복
while q:
    # 현재 강의
    now = q.popleft()

    # 다음 강의 탐색
    for i in graph[now]:
        # 최소 시간 구하기
        result[i] = max(result[i], result[now] + time[i])

        # 사전 강의 개수를 -1 시키고, 0이 되었다면 큐에 추가
        need[i] -= 1
        if need[i] == 0:
            q.append(i)

# 결과 출력
for i in range(1, N + 1):
    print(result[i])