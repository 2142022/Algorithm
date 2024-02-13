import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# x가 포함된 집합에서 가장 작은 수 구하기
def find(x):
    if min_num[x] != x:
        min_num[x] = find(min_num[x])
    return min_num[x]

#########################################################

# 두 집합 합치기
def connect(a, b):
    ma, mb = find(a), find(b)

    # 이미 같은 집합인 경우 패스
    if ma < mb:
        min_num[mb] = ma
    elif mb < ma:
        min_num[ma] = mb

#########################################################

# 초기 집합 수, 연산 수
n, m = map(int, input().split())

# 각 집합에서 가장 작은 숫자
min_num = [i for i in range(n + 1)]

# 연산
for _ in range(m):
    # 연산 종류, 두 원소
    op, a, b = map(int, input().split())

    # 두 집합 합치기
    if op == 0:
        connect(a, b)

    # 두 집합이 같은지 확인
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')