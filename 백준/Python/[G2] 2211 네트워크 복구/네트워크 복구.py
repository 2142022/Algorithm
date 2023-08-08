import heapq
import sys
input = sys.stdin.readline

# N: 컴퓨터 수, M: 회선 수
N, M = map(int, input().split())

# i번 컴퓨터가 가장 마지막으로 연결한 컴퓨터 번호
connect = [0] * (N + 1)

# 1번 컴퓨터와 i번 컴퓨터의 통신 시간
time = [2147483647] * (N + 1)

# 연결할 수 있는 회선 정보
# edges[1] = [(2, 1), (3, 2)]
# :1번 컴퓨터와 연결할 수 있는 컴퓨터는 2번, 3번이며,
#  2번 컴퓨터까지는 1, 3번 컴퓨터까지는 2만큼의 시간이 걸림
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    # A, B: 컴퓨터 번호, C: 통신 시간
    A, B, C = map(int, input().split())
    edges[A].append((B, C))
    edges[B].append((A, C))

# 통신 시간이 짧은 순서대로 edges 정보를 담은 최소 힙
h = []
# 1번 컴퓨터부터 시작
heapq.heappush(h, (0, 1))

# 최소 힙이 빌 때까지 반복
while h:
    # C: 통신 시간, A: 현재 컴퓨터 번호
    C, A = heapq.heappop(h)

    # A 컴퓨터와 연결된 컴퓨터들 탐색
    # i 컴퓨터와 A 컴퓨터의 통신 시간은 c
    for i, c in edges[A]:
        # A 컴퓨터를 거쳐서 1번 컴퓨터와 i 컴퓨터가 통신하는데 걸리는 시간
        t = C + c

        # 기존 통신 시간보다 작다면 갱신하고 최소 힙에 넣기
        if t < time[i]:
            time[i] = t
            connect[i] = A
            heapq.heappush(h, (t, i))

# 최종적으로 연결된 회선 정보
result = []
for i in range(2, N + 1):
    if connect[i] and (i, connect[i]) not in result and (connect[i], i) not in result:
        result.append((i, connect[i]))

# 결과 출력
print(len(result))
for a, b in result:
    print(a, b)
