import sys
from collections import deque

input = sys.stdin.readline

# x의 케빈 베이컨의 수 구하기
def get_cnt(x):
    # 다른 사람까지의 단계
    level = [0] * (N + 1)

    # 탐색할 사람을 담은 큐
    q = deque([x])
    while q:
        # 현재 사람
        p = q.popleft()
        l = level[p]

        # 연결된 사람 탐색
        for np in connect[p]:
            if not level[np]:
                level[np] = l + 1
                q.append(np)

    return sum(level)

###########################################################3

# 유저 수, 친구 관계 수
N, M = map(int, input().split())

# 친구 관계
connect = [list() for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    if A not in connect[B]:
        connect[A].append(B)
        connect[B].append(A)

# 가장 작은 케빈 베이컨의 수와 케빈 베이컨의 수가 가장 작은 사람
min_cnt, min_idx = N * M, 0

# 한 명씩 케빈 베이컨의 수 구하기
for i in range(1, N + 1):
    cnt = get_cnt(i)
    if cnt < min_cnt:
        min_cnt = cnt
        min_idx = i

print(min_idx)
