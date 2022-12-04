from itertools import combinations
import sys
input = sys.stdin.readline

# N: 도시의 크기, M: 선택할 수 있는 치킨집의 최대 개수
N, M = map(int, input().split())

# 집의 위치
house = []

# 치킨집의 위치
chicken = []

# 집과 치킨집의 위치 입력받기
for i in range(N):
    tmp = list(map(int, input().split()))

    for j in range(N):
        if tmp[j] == 1:
            house.append([i, j])
        elif tmp[j] == 2:
            chicken.append([i, j])

# 도시의 치킨 거리의 최솟값
result = 2147483647

# M개의 치킨집 뽑기(조합)
for comb in combinations(chicken, M):
    # 도시의 치킨 거리
    total = 0
    
    # 집마다 가장 가까운 치킨집과의 거리 구하기
    for h in house:
        # 가장 가까운 치킨집과의 거리
        min_len = 2147483647

        for c in comb:
            min_len = min(min_len, abs(h[0] - c[0]) + abs(h[1] - c[1]))

        total += min_len

    result = min(result, total)

print(result)
