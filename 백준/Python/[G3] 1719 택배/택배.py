import sys
input = sys.stdin.readline

# n: 집하장의 개수, m: 집하장 간 경로의 개수
n, m = map(int, input().split())

# 집하장 간 이동 시간
time = [[2147483647] * (n + 1) for _ in range(n + 1)]
# 경로표
result = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    # c: 집하장 a, b 사이를 오가는데 필요한 시간
    a, b, c = map(int, input().split())
    time[a][b] = time[b][a] = c
    result[a][b] = b
    result[b][a] = a

# 플로이드 워셜
# 거쳐가는 집하장
for k in range(1, n + 1):
    # 출발 집하장
    for i in range(1, n + 1):
        # 도착 집하장
        for j in range(1, n + 1):
            if i == j:
                continue

            # k를 거치는 경우와 거치지 않는 경우의 시간 비교
            if time[i][k] + time[k][j] < time[i][j]:
                result[i][j] = result[i][k]
                time[i][j] = time[i][k] + time[k][j]

# 경로표 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print('-', end = ' ')
        else:
            print(result[i][j], end = ' ')
    print()