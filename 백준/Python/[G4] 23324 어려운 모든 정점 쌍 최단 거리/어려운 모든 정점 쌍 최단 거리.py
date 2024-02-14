from collections import defaultdict
import sys
input = sys.stdin.readline

# x와 연결된 노드 중 가장 작은 번호 구하기
def find(x):
    if min_node[x] != x:
        min_node[x] = find(min_node[x])
    return min_node[x]

#######################################################################

# 두 노드 연결하기
def connect(a, b):
    ma, mb = find(a), find(b)

    # 이미 연결되어 있는 경우 끝내기
    if ma == mb:
        return

    if ma < mb:
        min_node[mb] = ma
    else:
        min_node[ma] = mb

#######################################################################

# 노드 수, 간선 수, 가중치가 있는 간선
N, M, K = map(int, input().split())

# 가중치가 없는 간선으로 연결된 노드 중 가장 작은 번호
min_node = [i for i in range(N + 1)]

# 가중치가 없는 간선으로 연결된 노드들만 연결하기
for i in range(1, M + 1):
    u, v = map(int, input().split())

    # 가중치가 있는 경우 패스
    if i == K:
        continue

    # 두 노드 연결하기
    connect(u, v)

# 각 집합의 원소 개수
cnt = defaultdict(int)
for i in range(1, N + 1):
    cnt[find(i)] += 1

# 모든 원소가 이어져 있는 경우 최단 거리의 합은 0
if len(cnt) == 1:
    print(0)

# 모든 원소가 이어져 있지 않은 경우, 집합은 2개
# 집합의 원소 개수의 곱이 답
else:
    result = 1
    for i in cnt.values():
        result *= i
    print(result)
