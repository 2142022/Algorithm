from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 컴퓨터 x와 연결된 컴퓨터 중 가장 작은 번호
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

##############################################################

# 두 컴퓨터 연결하기
def connect(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

##############################################################

# 컴퓨터 개수, 연결 쌍의 개수
n, m = map(int, input().split())

# 연결된 컴퓨터들 중 가장 작은 컴퓨터 번호
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    connect(a, b)

# 두 컴퓨터 연결 비용과 두 컴퓨터 번호를 담은 최소 힙
h = []

# 연결 비용 탐색
for i in range(1, n + 1):
    info = list(map(int, input().split()))

    # 1번 컴퓨터를 제외하고 연결 비용을 힙에 추가
    # 1번 컴퓨터는 메인 컴퓨터로, 모든 컴퓨터와 연결되어 있음
    if i != 1:
        for j in range(i + 1, n + 1):
            heappush(h, (info[j - 1], i, j))

# 안정적인 네트워크를 만드는데 필요한 비용
cost = 0
# 연결 간선 정보 (1번 컴퓨터를 제외하므로 총 간선은 n-2개)
cnt = 0
# 새로 연결하는 쌍
pair = []

# 안정적인 네트워크가 만들어질 때까지 반복
while h and cnt != n - 2:
    # 비용, 두 컴퓨터(a, b)
    c, a, b = heappop(h)

    # 두 컴퓨터 연결하기
    if find_parent(a) != find_parent(b):
        cost += c
        cnt += 1
        pair.append((a, b))
        connect(a, b)

print(cost, len(pair))
for a, b in pair:
    print(a, b)

