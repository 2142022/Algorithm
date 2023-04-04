import sys
input = sys.stdin.readline

# 굴다리의 길이
N = int(input())

# 가로등의 개수
M = int(input())

# M개의 가로등의 위치
location = list(map(int, input().split()))

# 가로등의 최소 높이
# 첫 번째 가로등까지의 거리로 초기화
result = location[0] - 0

# 두 번째 가로등부터는 가로등 사이의 거리 / 2 (올림)
for i in range(1, M):
    result = max(result, (location[i] - location[i - 1] + 1) // 2)

# 마지막 가로등은 굴다리 끝까지 비춰야 함
result = max(result, N - location[M - 1])

print(result)
