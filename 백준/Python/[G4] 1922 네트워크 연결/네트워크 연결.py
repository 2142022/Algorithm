from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# x와 연결된 컴퓨터 중 제일 작은 컴퓨터 번호 구하기
def find(x):
    if min_com[x] != x:
        min_com[x] = find(min_com[x])
    return min_com[x]

#####################################################

# 두 컴퓨터 연결하기
def connect(a, b):
    ma, mb = find(a), find(b)

    # 이미 연결되어 있는 경우 끝내기
    if ma == mb:
        return False

    # 더 작은 번호로 저장
    if ma < mb:
        min_com[mb] = ma
    else:
        min_com[ma] = mb
    return True

#####################################################

# 컴퓨터 수
N = int(input())

# 연결되어 있는 컴퓨터 중 가장 작은 번호
min_com = [i for i in range(N + 1)]

# 연결할 수 있는 선의 수
M = int(input())

# 탐색 선을 담은 최소 힙
h = []
for _ in range(M):
    a, b, c = map(int, input().split())
    heappush(h, (c, a, b))

# 연결한 선의 개수
cnt = 0

# 모든 컴퓨터를 연결하는데 필요한 최소 비용
cost = 0

# 최소 비용인 선 찾아서 연결하기
while h:
    # 모든 컴퓨터를 연결한 경우 끝내기
    if cnt == N - 1:
        break

    # 비용, 두 컴퓨터
    c, a, b = heappop(h)

    # 두 컴퓨터가 연결되어 있지 않은 경우, 연결하기
    if connect(a, b):
        cnt += 1
        cost += c

print(cost)