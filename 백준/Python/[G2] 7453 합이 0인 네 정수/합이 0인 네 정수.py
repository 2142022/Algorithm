from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

# 배열의 크기
n = int(input())

# 4개의 배열
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# A + B, C + D
AB, CD = [], []
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

# 오름차순 정렬
AB.sort()
CD.sort()

# 합이 0이 되는 쌍의 개수
cnt = 0

# AB의 인덱스, CD의 인덱스
idx1, idx2 = 0, len(CD) - 1

# AB, CD 탐색
while idx1 < len(AB) and idx2 >= 0:
    # A + B, C + D
    ab, cd = AB[idx1], CD[idx2]
    # A + B + C + D
    num = ab + cd

    # 0보다 크다면 C + D 감소
    if num > 0:
        idx2 -= 1

    # 0보다 작다면 A + B 증가
    elif num < 0:
        idx1 += 1

    # 0이라면 (A+B의 개수) * (C+D의 개수)를 cnt에 추가
    else:
        # (A + B)의 개수
        cntAB = bisect_right(AB, ab) - bisect_left(AB, ab)
        # (C + D)의 개수
        cntCD = bisect_right(CD, cd) - bisect_left(CD, cd)

        # cnt 갱신
        cnt += cntAB * cntCD

        # 인덱스 갱신
        idx1 += cntAB
        idx2 -= cntCD

print(cnt)