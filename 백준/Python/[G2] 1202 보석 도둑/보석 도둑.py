from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 보석 개수, 가방 개수
N, K = map(int, input().split())

# 각 보석의 무게와 가격 (무게 기준 오름차순 정렬)
M = sorted([list(map(int, input().split())) for _ in range(N)])

# 가방이 담을 수 있는 최대 무게 (오름차순 정렬)
C = sorted([int(input()) for _ in range(K)])

# 상덕이가 훔칠 수 있는 보석의 최대 합
s = 0

# 탐색하는 가방에 넣을 수 있는 보석을 담은 최대 힙 (가격 기준)
V = []

# 최대 힙에 넣은 마지막 보석의 인덱스 + 1
i = 0

# 현재 가방이 담을 수 있는 최대 무게
for c in C:
    # 현재 가방에 담을 수 있는 보석 모두 담기
    while i < N and M[i][0] <= c:
        m, v = M[i]
        heappush(V, (-v, m))
        i += 1

    # 현재 가방에 담을 수 있는 보석이 있는 경우
    if V:
        # V는 최대 힙이므로 음수로 저장되어 있음
        s -= heappop(V)[0]

print(s)
