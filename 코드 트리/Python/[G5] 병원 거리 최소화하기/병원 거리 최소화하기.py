import sys
input = sys.stdin.readline

# 병원 하나씩 선택하기
# i: 현재 병원
# cnt: 선택한 병원 수
def select(i, cnt):
    global min_sum, dist

    # m개의 병원을 모두 선택한 경우
    if cnt == m:
        min_sum = min(min_sum, sum(dist))
        # 모든 사람이 갈 수 있는 최단 거리인 경우 끝내기
        if min_sum == min_time_sum:
            return 1
        return 0

    # 현재 병원을 선택하지 않는 경우
    if H - i + cnt > m:
        if select(i + 1, cnt):
            return 1

    # 현재 병원을 선택하는 경우
    dist_copy = dist[:]
    for p in range(P):
        dist[p] = min(dist[p], time[p][i])
    if select(i + 1, cnt + 1):
        return 1
    dist = dist_copy

    return 0

##################################################################

# 도시 크기, 남길 병원 개수
n, m = map(int, input().split())

# 사람 위치, 병원 위치
people, hospital = [], []
for i in range(n):
    row = list(map(int, input().split()))
    for j, info in enumerate(row):
        if info == 1:
            people.append((i, j))
        elif info == 2:
            hospital.append((i, j))

# 사람 수, 병원 수
P, H = len(people), len(hospital)

# 각 사람이 각 병원까지 가는데 걸리는 시간
time = [[0] * H for _ in range(P)]
# 모든 사람이 갈 수 있는 최단 거리 합
min_time_sum = 0
for i in range(P):
    # 사람 위치
    pr, pc = people[i]

    # 현재 사람과 가장 가까운 병원까지의 시간
    min_time = 2 * n
    for j in range(H):
        # 병원 위치
        hr, hc = hospital[j]
        time[i][j] = abs(hr - pr) + abs(hc - pc)
        min_time = min(min_time, time[i][j])
    min_time_sum += min_time

# 병원 m개를 남겼을 때 가능한 각 사람들의 병원 거리 총 합 중 최솟값
min_sum = 2 * P * n

# 각 사람이 갈 수 있는 병원까지의 최단 거리
dist = [2 * n] * P

# 병원 하나씩 선택하기
select(0, 0)

print(min_sum)