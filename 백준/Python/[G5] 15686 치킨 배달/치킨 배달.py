import sys
input = sys.stdin.readline

# 치킨집 하나씩 선택하기
# cnt: 선택한 치킨집 수
# start: 현재 선택가능한 치킨집 중 최소 번호
def select(cnt, start, dist):
    global min_sum

    # m개의 치킨집을 모두 선택한 경우
    if cnt == M:
        min_sum = min(min_sum, sum(dist))
        # 모든 사람이 갈 수 있는 최단 거리인 경우 끝내기
        if min_sum == limit:
            return 1
        return 0

    # 치킨집 선택
    for i in range(start, C - M + cnt + 1):
        # 현재까지의 거리 저장
        dist_copy = dist[:]
        for p in range(P):
            dist_copy[p] = min(dist_copy[p], info[p][i])
        if select(cnt + 1, i + 1, dist_copy):
            return 1

    return 0

##################################################################

# 도시 크기, 남길 치킨집 개수
N, M = map(int, input().split())

# 사람 위치, 치킨집 위치
people, chicken = [], []
for i in range(N):
    row = list(map(int, input().split()))
    for j, info in enumerate(row):
        if info == 1:
            people.append((i, j))
        elif info == 2:
            chicken.append((i, j))

# 사람 수, 치킨집 수
P, C = len(people), len(chicken)

# 각 사람이 각 치킨집까지의 거리
info = [[0] * C for _ in range(P)]
# 모든 사람이 갈 수 있는 최단 거리 합
limit = 0
for i in range(P):
    # 사람 위치
    pr, pc = people[i]

    # 현재 사람과 가장 가까운 치킨집까지의 거리
    for j in range(C):
        # 치킨집 위치
        cr, cc = chicken[j]
        info[i][j] = abs(cr - pr) + abs(cc - pc)
    limit += min(info[i])

# 치킨집 m개를 남겼을 때 가능한 각 사람들의 치킨집 거리 총 합 중 최솟값
min_sum = 2 * P * N

# 각 사람이 갈 수 있는 치킨집까지의 최단 거리
dist = [2 * N] * P

# 치킨집 하나씩 선택하기
select(0, 0, dist)

print(min_sum)