import sys
input = sys.stdin.readline

# 마을 개수, 도로 개수
V, E = map(int, input().split())

# 마을 간 거리
dist = [[sys.maxsize] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

# 최소 사이클 경로 길이
result = sys.maxsize

# 거쳐가는 마을
for k in range(1, V + 1):
    # 출발 마을
    for i in range(1, V + 1):
        # 도착 마을
        for j in range(1, V + 1):
            if i != j and dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

            # 사이클이 있는 경우
            if dist[i][j] != sys.maxsize and dist[j][i] != sys.maxsize:
                result = min(result, dist[i][j] + dist[j][i])

# 사이클이 없는 경우
if result >= sys.maxsize:
    result = -1

print(result)