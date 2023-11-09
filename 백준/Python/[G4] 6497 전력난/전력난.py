from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 연결된 집 중 가장 작은 번호 구하기
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

###################################################################

# 테스트 케이스
while True:
    # 집의 수, 길의 수
    m, n = map(int, input().split())

    # 더 이상 테스트 케이스가 없는 경우
    if m == 0 and n == 0:
        break

    # 모든 도로의 길이(비용)
    total = 0

    # 도로 정보 (x번 집과 y번 집 사이에 z미터 도로가 있음을 의미)
    road = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        total += z
        heappush(road, (z, x, y))

    # 연결된 집들 중 가장 작은 번호
    parent = [i for i in range(m)]

    # 연결한 도로 개수
    cnt = 0
    # 연결한 도로 길이(비용) 합
    cost = 0

    # 도로 연결하기
    while road:
        # x번 집과 y번 집을 연결하는 z미터 도로
        z, x, y = heappop(road)

        # 각 집에 연결된 집 중 가장 작은 번호
        px = find_parent(x)
        py = find_parent(y)

        # 이미 두 집이 연결되어 있는 경우 패스
        if px == py:
            continue

        # 두 집 연결하기
        if px < py:
            parent[py] = px
        else:
            parent[px] = py
        cnt += 1
        cost += z

        # 모든 집을 연결한 경우 끝내기
        if cnt == m - 1:
            break

    # 최대 절약 비용
    print(total - cost)