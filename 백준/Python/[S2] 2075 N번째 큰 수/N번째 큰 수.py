import heapq
import sys
input = sys.stdin.readline

# 문제: N X N의 표에서 N번째 큰 수 찾기
N = int(input())

# 우선순위 큐 (최소 힙)
# 크기를 N으로 유지하기
q = []

# 큐에 원소 넣기
for i in range(N):
    tmp = list(map(int, input().split()))

    # 큐의 크기가 N보다 작을 때는 그냥 넣기
    if len(q) < N:
        for num in tmp:
            heapq.heappush(q, num)

    # 큐의 크기가 N보다 크다면 큐의 가장 작은 원소보다 클 때만 넣기
    else:
        for num in tmp:
            if num > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, num)

# 큐의 길이를 N으로 유지하였기 때문에 큐의 가장 작은 원소를 뽑으면 됨
print(q[0])
