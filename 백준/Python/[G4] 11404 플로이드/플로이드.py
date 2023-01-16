import sys
input = sys.stdin.readline

# 도시의 개수
n = int(input())

# 버스의 개수
m = int(input())

# cost[i][j] = k: 도시 i에서 도시 j로 가는데 필요한 비용
# cost[i][i] = 0: 자기 자신으로 가는 비용은 0
cost = [[2147483647] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    cost[i][i] = 0

# 버스 정보 입력받기
for _ in range(m):
    # a: 버스 시작 도시, b: 버스 도착 도시, c: 필요 비용
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

# 플로이드 워셜 알고리즘
# i: 거쳐가는 도시, j: 출발 도시, k: 도착 도시
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])

# 모든 도시에서 도시로가는 비용 구하기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 갈 수 없는 경우에는 0 출력
        if cost[i][j] == 2147483647:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')

    print()