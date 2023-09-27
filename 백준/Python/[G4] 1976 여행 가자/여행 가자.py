import sys
input = sys.stdin.readline

# 도시 수
N = int(input())
# 여행 계획에 속한 도시 수
M = int(input())

# 도시 연결 정보
connect = [list(map(int, input().split())) for _ in range(N)]

# 플로이드 워셜로 연결된 모든 도시 갱신
# 거쳐가는 도시
for k in range(N):
    # 시작 도시
    for i in range(N):
        # 도착 도시
        for j in range(N):
            if not connect[i][j] and connect[i][k] and connect[k][j]:
                connect[i][j] = connect[j][i] = 1

# 여행 계획
plan = list(map(int, input().split()))

# 여행 계획 가능 여부 확인
possible = 1
for i in range(1, M):
    a, b = plan[i - 1] - 1, plan[i] - 1
    if a != b and not connect[a][b]:
        possible = 0
        break

if possible:
    print("YES")
else:
    print("NO")