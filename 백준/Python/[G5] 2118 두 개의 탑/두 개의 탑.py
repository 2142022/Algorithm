import sys
input = sys.stdin.readline

# 지점 수
N = int(input())

# 두 지점 사이 거리 (누적합)
dist = [0] * (N + 1)
for i in range(1, N + 1):
    dist[i] = dist[i - 1] + int(input())

# 총 거리
total = dist[-1]

# 두 탑 거리의 최댓값
max_dist = 0

# 도착 지점
end = 1

# 시작 지점
for start in range(N):
    # 시계 방향 거리가 반시계 방향 거리보다 작을 때까지만 탐색
    # 마지막 위치가 둘의 차이가 최소가 되므로, 최대 거리가 나옴
    while end <= N and dist[end] - dist[start] <= total - dist[end] + dist[start]:
        max_dist = max(max_dist, dist[end] - dist[start])
        end += 1

print(max_dist)