from collections import deque
import sys
input = sys.stdin.readline

# W를 건설하는데 필요한 최소 시간 구하기
def build(W):
    # 각 건물을 짓는데 필요한 최소 시간 (W부터 거꾸로)
    time = [0] * (N + 1)
    time[W] = D[W]

    # W 건물을 짓는데 필요한 최소 시간
    min_time = D[W]

    # 건물과 현재까지의 시간을 담은 큐
    q = deque([(W, D[W])])
    while q:
        # 현재 건물, 현재까지의 시간
        i, t = q.popleft()

        # 현재 건물을 짓는데 필요한 최소 시간과 다르다면 패스
        if t != time[i]:
            continue
        min_time = max(min_time, t)

        # 현재 건물을 짓기 이전에 지어야 하는 건물 탐색
        for ni in prev[i]:
            nt = D[ni]

            # 기록된 시간보다 작다면 패스
            if t + nt <= time[ni]:
                continue

            time[ni] = t + nt
            q.append((ni, t + nt))

    return min_time

###############################################################

# 테스트 케이스
for _ in range(int(input())):
    # 건물 개수, 건설 순서 규칙
    N, K = map(int, input().split())

    # 각 건물의 건설 시간
    D = [0] + list(map(int, input().split()))

    # 각 건물을 짓기 이전에 지어야 하는 건물들
    prev = [list() for _ in range(N + 1)]

    # 건설순서 (건물 X를 지은 다음에 건물 Y를 짓는 것이 가능)
    for _ in range(K):
        X, Y = map(int, input().split())
        prev[Y].append(X)

    # 백준이가 건설할 건물
    W = int(input())

    # W를 건설하는데 필요한 최소 시간
    print(build(W))
