from itertools import combinations
from collections import defaultdict
import sys
input = sys.stdin.readline

# 현재 선거구의 인구수
def get_pop(A):
    M = len(A)

    # 연결된 사람들 체크
    v = [[0] * M for _ in range(M)]

    # 모두 연결되어 있는지 확인
    i = 0
    while i < M:
        n1 = A[i]
        v[i][i] = 1

        # 연결된 사람들 체크
        for j in range(i + 1, M):
            n2 = A[j]

            if n1 in connect[n2]:
                v[i][j] = v[j][i] = 1
        i += 1

    # 플로이드 워셜
    for k in range(M):
        for i in range(M):
            for j in range(M):
                if v[i][k] and v[k][j]:
                    v[i][j] = v[i][k] + v[k][j]

    # 한 명이라도 안 연결되어 있는 경우
    if 0 in v[0]:
        return 0

    # 인구 수 합 구하기
    s = 0
    for i in A:
        s += population[i]
    return s

########################################################################

# 구역 수
N = int(input())

# 각 구역의 인구 수
population = [0] + list(map(int, input().split()))

# 연결되어 있는 구역 수와 번호
connect = defaultdict(list)
for i in range(1, N + 1):
    cnt, *idx = map(int, input().split())
    if cnt:
        connect[i] = idx

# 최소 인구수 차이
min_diff = 1000

# 한 선거구의 개수
for cnt in range(1, N // 2 + 1):
    # 한 선거구의 구역
    for combs1 in combinations(range(1, N + 1), cnt):
        # 다른 선거구
        combs2 = [i for i in range(1, N + 1) if i not in combs1]

        # 두 선거구의 인구수
        p1, p2 = get_pop(list(combs1)), get_pop(combs2)

        # 만약 모두 연결되어 있는 경우
        if p1 and p2:
            min_diff = min(min_diff, abs(p1 - p2))

            if min_diff == 0:
                break
    if min_diff == 0:
        break

if min_diff == 1000:
    print(-1)
else:
    print(min_diff)