import heapq
import sys
input = sys.stdin.readline

# N: 도시의 개수, M: 통로의 개수, C: 메시지를 보내고자 하는 도시
N, M, C = map(int, input().split())

# 각 도시에 연결되어 있는 도시에 대한 정보
# path[X] = [(Y, Z)]: 도시 X에서 도시 Y로 메시지를 전달하는 시간 Z
path = [[] for _ in range(N + 1)]

# 메세지 전송 최단 시간
time = [2147483647] * (N + 1)

# 연결 도시 정보 입력받기
# X: 메시지 출발 도시
# Y: 메시지 도착 도시
# Z: 메세지 전달 시간
for _ in range(M):
    X, Y, Z = map(int, input().split())
    path[X].append((Y, Z))

# 우선순위 큐를 이용하여 짧은 시간 순으로 메시지 전달
queue = []
# C부터 시작
heapq.heappush(queue, (0, C))
time[C] = 0

# 큐가 빌 때까지 반복
while queue:
    # 가장 짧은 시간으로 전달 가능한 도시 꺼내기
    t, n = heapq.heappop(queue)

    # 이미 확인한 도시라면 패스
    if time[n] < t:
        continue

    # 현재 도시와 연결된 다른 도시들 탐색
    for i in path[n]:
        # 현재 도시를 거쳐서 전달되는 시간
        temp_time = t + i[1]

        # 기존 시간보다 작다면 갱신하고 큐에 넣기
        if temp_time < time[i[0]]:
            time[i[0]] = temp_time
            heapq.heappush(queue, (temp_time, i[0]))

# 메시지를 받는 도시의 총 개수
cnt = 0

# 총 걸리는 시간
total_time = 0

for i in range(1, N + 1):
    # 메시지를 보낸 도시는 패스
    if i == C:
        continue

    if time[i] != 2147483647:
        cnt += 1
        total_time = max(total_time, time[i])

print(cnt, total_time)