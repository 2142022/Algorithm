from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 집 x와 연결된 집 중 가장 작은 번호 구하기
def find_house(x):
    if min_idx[x] != x:
        min_idx[x] = find_house(min_idx[x])
    return min_idx[x]

########################################################################

# 집 x, y 연결하기
def connect(x, y):
    x, y = find_house(x), find_house(y)

    # 이미 연결되어 있는 경우
    if x == y:
        return False

    # 연결하기
    if x < y:
        min_idx[y] = x
    else:
        min_idx[x] = y
    return True

########################################################################

# 집 개수, 길 개수
N, M = map(int, input().split())

# 유지비, 두 집을 담은 최소 힙
h = []
for _ in range(M):
    A, B, C = map(int, input().split())
    heappush(h, (C, A, B))

# 각 집에 연결된 집 중 가장 작은 번호
min_idx = [i for i in range(N + 1)]

# 연결한 간선 개수
cnt = 0

# 연결한 간선 중 가장 큰 유지비
max_cost = 0

# 연결한 모든 유지비의 합
s = 0

# 모든 집 연결하기
while h:
    # 가장 작은 유지비를 가진 간선
    C, A, B = heappop(h)

    # 두 집 연결하기
    if connect(A, B):
        cnt += 1
        max_cost = C
        s += C

        # 모든 집을 연결한 경우 끝내기
        if cnt == N - 1:
            break

# 두 마을로 분리하기 위해, 가장 유지비가 큰 간선 지우기
print(s - max_cost)