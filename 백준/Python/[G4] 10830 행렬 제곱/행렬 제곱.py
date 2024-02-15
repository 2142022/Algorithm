from collections import defaultdict
import sys
input = sys.stdin.readline

# A의 x제곱, A의 y제곱 곱하기
def multi(x, y):
    # 나눌 수
    m = 1000

    # A의 (x + y)제곱
    result = [[0] * N for _ in range(N)]
    for i, row in enumerate(square[x]):
        for j, col in enumerate(list(map(list, zip(*square[y])))):
            for k in range(N):
                result[i][j] += (row[k] * col[k]) % m
            result[i][j] %= m

    square[x + y] = result
    return x + y

#####################################################################################

# A의 x제곱 구하기
def solve(x):
    # 이전에 A의 x제곱을 구한 적이 있는 경우
    if x in square:
        return

    # 반으로 나눠서 곱하기
    mid = x // 2
    solve(mid)
    if x % 2 == 0:
        multi(mid, mid)
    else:
        multi(multi(mid, mid), 1)

#####################################################################################

# 행렬 크기, 행렬을 제곱할 수
N, B = map(int, input().split())

# 행렬
A = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(N)]

# square[i]: A를 i번 제곱했을 때의 행렬
square = defaultdict(list)
square[1] = A

# A의 B제곱 구하기
solve(B)

for i in square[B]:
    print(*i)
