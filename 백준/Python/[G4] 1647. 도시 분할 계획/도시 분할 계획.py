import heapq
import sys
input = sys.stdin.readline

# x번 집과 연결된 집 중 대표 집 찾기
def find_parent(x):
    # 재귀로 대표 집 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

#######################################

# N: 집의 개수, M: 길의 개수
N, M = map(int, input().split())

# 집과 연결된 집 중 대표 집 번호
# 처음에는 자기 자신으로 초기화
parent = [i for i in range(N + 1)]

# 길의 정보가 담긴 리스트
path = []
for _ in range(M):
    # A번 집과 B번 집을 연결하는 길의 유지비가 C
    A, B, C = map(int, input().split())

    # 유지비가 작은 순으로 담기
    heapq.heappush(path, (C, A, B))

# 최종적으로 연결되는 길들의 유지비
total_cost = 0
# 최종적으로 연결되는 길 중 가장 큰 유지비
max_cost = 0

# 모든 길의 정보 확인
while path:
    C, A, B = heapq.heappop(path)

    # A, B가 아직 연결되어 있지 않는 경우에만 추가
    if find_parent(A) != find_parent(B):
        parent[find_parent(B)] = find_parent(A)
        total_cost += C
        max_cost = max(max_cost, C)

print(total_cost - max_cost)