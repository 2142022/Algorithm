from collections import defaultdict
import sys
input = sys.stdin.readline

# 배열 크기
n = int(input())

# 각 배열 (오름차순 정렬)
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
A.sort()
B.sort()
C.sort()
D.sort()

# 합이 0이 되는 쌍의 개수
cnt = 0

# A + B의 모든 경우 (오름차순 정렬)
AB = []
# C + D의 모든 경우 (오름차순 정렬)
CD = []
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])
AB.sort()
CD.sort()

# AB, CD 크기
m = len(AB)

# A + B의 인덱스, C + D의 인덱스
abi, cdi = 0, m - 1
while abi < m and cdi >= 0:
    # a + b, c + d
    ab, cd = AB[abi], CD[cdi]

    # 네 수의 합
    s = ab + cd

    # 네 수의 합이 0인 경우
    if s == 0:
        # 현재 a + b의 개수
        ab_cnt = 0
        while abi < m and AB[abi] == ab:
            abi += 1
            ab_cnt += 1

        # 현재 c + d의 개수
        cd_cnt = 0
        while cdi >= 0 and CD[cdi] == cd:
            cdi -= 1
            cd_cnt += 1

        # 합이 0인 개수
        cnt += ab_cnt * cd_cnt

    # 네 수의 합이 양수인 경우, C + D 줄이기
    elif s > 0:
        cdi -= 1

    # 네 수의 합이 음수인 경우, A + B 늘리기
    else:
        abi += 1

print(cnt)