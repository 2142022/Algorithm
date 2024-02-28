from collections import defaultdict
import sys
input = sys.stdin.readline

# 수의 개수
N = int(input())

# N개의 수
A = sorted(list(map(int, input().split())))

# 최댓값
max_num = A[-1]

# 각 수의 위치
pos = defaultdict(list)
for i, a in enumerate(A):
    pos[a].append(i)

# 좋은 수 개수
cnt = 0

# 두 수의 합
for i in range(N - 1):
    n1 = A[i]
    for j in range(i + 1, N):
        n2 = A[j]
        s = n1 + n2

        # 최댓값을 넘어간 경우 패스
        if s > max_num:
            break

        # 좋은 수인 경우
        if s in pos:
            # 아직 체크를 안 한 경우
            for k in range(len(pos[s]) - 1, -1, -1):
                idx = pos[s][k]
                if idx != i and idx != j:
                    pos[s].pop(k)
                    cnt += 1

print(cnt)