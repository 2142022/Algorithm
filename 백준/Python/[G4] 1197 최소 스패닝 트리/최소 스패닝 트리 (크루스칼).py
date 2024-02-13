from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# x와 연결된 노드 중 가장 작은 노드 구하기
def find(x):
    if min_idx[x] != x:
        min_idx[x] = find(min_idx[x])
    return min_idx[x]

#######################################################

# 두 노드 연결하기
def connect(a, b):
    ma, mb = find(a), find(b)

    # 이미 연결되어 있는 경우 패스
    if ma == mb:
        return False

    if ma < mb:
        min_idx[mb] = ma
    else:
        min_idx[ma] = mb
    return True

#######################################################

# 노드 개수, 간선 개수
V, E = map(int, input().split())

# 가중치와 두 노드 정보를 담은 최소 힙
h = []
for _ in range(E):
    A, B, C = map(int, input().split())
    heappush(h, (C, A, B))

# 연결된 노드 중 가장 작은 노드 번호
min_idx = [i for i in range(V + 1)]

# 최소 스패닝 트리의 가중치, 연결된 간선 개수
mst = cnt = 0

# 가장 작은 가중치를 가진 간선 뽑기
while h:
    # 최소 스패닝 트리가 만들어진 경우 끝내기
    if cnt == V - 1:
        break

    # 가장 작은 가중치를 가진 간선과 두 노드
    w, u, v = heappop(h)

    # 두 노드가 연결되어 있지 않은 경우 연결
    if connect(u, v):
        mst += w
        cnt += 1

print(mst)