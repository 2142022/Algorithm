import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 부모 뉴런을 찾는 함수
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

###############################################

# N: 뉴런의 개수, M: 시냅스의 개수
N, M = map(int, input().split())

# 각 뉴런의 부모 뉴런
parent = [i for i in range(N + 1)]

# 연결을 끊는 횟수
cnt = 0

# M개의 시냅스 정보 입력 받기
for _ in range(M):
    u, v = map(int, input().split())

    # 두 뉴런이 이미 연결되어 있다면 싸이클이므로 연결 끊기
    if find_parent(u) == find_parent(v):
        cnt += 1

    # 연결시키기
    else:
        parent[find_parent(u)] = find_parent(v)

# 최상위 부모 뉴런으로 바꾸기
for i in range(1, N + 1):
    find_parent(i)

# 결과값(모든 뉴런을 연결하기 위해 필요한 최소 연산 횟수): 부모 뉴런의 개수 - 1 + 연결을 끊는 횟수
# 인덱스 0 때문에 1을 더 빼야 함
print(cnt + len(set(parent)) - 2)