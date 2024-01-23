import sys
input = sys.stdin.readline

# 아홉 난쟁이의 키
H = []
# 일곱 난쟁이가 아닌 두 명의 키 합
K = -100
for _ in range(9):
    n = int(input())
    H.append(n)
    K += n
H.sort()

# 일곱 난쟁이가 아닌 두 명 찾기
idx1, idx2 = 0, 8
while True:
    n1, n2 = H[idx1], H[idx2]

    # 두 명의 키가 K보다 작다면 다음으로 큰 키 찾기
    if n1 + n2 < K:
        idx1 += 1
    # 두 명의 키가 K보다 작다면 다음으로 작은 키 찾기
    elif n1 + n2 > K:
        idx2 -= 1
    # 두 명을 찾은 경우 끝내기
    else:
        break

for i in range(9):
    if i != idx1 and i != idx2:
        print(H[i])