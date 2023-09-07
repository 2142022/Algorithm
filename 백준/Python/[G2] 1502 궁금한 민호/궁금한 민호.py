import copy
import sys
input = sys.stdin.readline

# 도시의 개수
N = int(input())

# 도시 A에서 도시 B로 이동하는데 필요한 시간
times = [list(map(int, input().split())) for _ in range(N)]

# 사용하는 도로의 시간
used = copy.deepcopy(times)

# 거쳐가는 도시
for k in range(N):
    # 출발 도시
    for i in range(N):
        # 도착 도시
        for j in range(N):
            # 기존의 최단 경로보다 더 짧은 거리가 있다면 불가능하므로 끝내기
            if times[i][j] > times[i][k] + times[k][j]:
                print(-1)
                exit()

            # 거쳐가는 도시가 출발 도시나 도착 도시와 같다면 패스
            if k == i or k == j:
                continue

            # 기존의 최단 경로와 같은 경우가 있다면 도로를 줄일 수 있음
            elif times[i][j] == times[i][k] + times[k][j]:
                used[i][j] = 0

# 최소한의 도로만 사용했을 때의 시간
result = 0
for i in range(N):
    for j in range(i + 1, N):
        result += used[i][j]

print(result)