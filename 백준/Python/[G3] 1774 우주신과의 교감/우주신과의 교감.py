from itertools import combinations
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# x와 연결된 신들 중 가장 작은 인덱스 찾기
def find_rep(x):
    if rep[x] != x:
        rep[x] = find_rep(rep[x])
    return rep[x]

################################################################################################

# 두 신 연결하기 - 연결 여부 반환
def union(a, b):
    ra, rb = find_rep(a), find_rep(b)
    if ra == rb:
        return False
    if ra < rb:
        rep[rb] = ra
    elif rb < ra:
        rep[ra] = rb
    return True

################################################################################################

# 우주신 수, 통로 개수
N, M = map(int, input().split())

# 우주신 좌표
pos = [list()] + [list(map(int, input().split())) for _ in range(N)]

# 우주신 사이에 연결 통로 개수
cnt = 0

# 연결된 우주신들 중 가장 작은 인덱스
rep = [i for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    # 아직 연결되어 있지 않은 경우, 연결하기
    if union(a, b):
        cnt += 1

# 두 신 사이에 연결해야 할 통로 길이와 두 신의 번호를 담은 최소 힙
h = []
for a, b in combinations(range(1, N + 1), 2):
    # 아직 연결이 되어 있지 않은 경우 힙에 넣기
    if find_rep(a) != find_rep(b):
        l = ((pos[a][0] - pos[b][0]) ** 2 + (pos[a][1] - pos[b][1]) ** 2) ** 0.5
        heappush(h, (l, a, b))

# 만들어야 할 최소 통로 길이
total = 0

# 모든 신들이 연결될 때까지 반복
while h and cnt < N - 1:
    # 만들어야 할 통로 길이, 두 신의 번호
    l, a, b = heappop(h)

    # 아직 연결이 되어 있지 않은 경우 연결
    if union(a, b):
        total += l
        cnt += 1

print(f'{total:.2f}')