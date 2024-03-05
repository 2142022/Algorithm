import sys
input = sys.stdin.readline

# 정점 개수
N = int(input())

# 인접 행렬
connect = [list(map(int, input().split())) for _ in range(N)]

# 플로이드 워셜
for k in range(N):
    for i in range(N):
        for j in range(N):
            if connect[i][k] and connect[k][j]:
                connect[i][j] = max(connect[i][j], connect[i][k] + connect[k][j])

# 경로가 있으면 1, 없으면 0 출력
for c in connect:
    print(*list(map(lambda x: 1 if x else 0, c)))
