import sys
input = sys.stdin.readline

# N: 회사 개수, M: 경로 개수
N, M = map(int, input().split())

# 연결 리스트 (연결된 회사는 1, 자기 자신으로 가는 경로는 0으로 초기화)
path = [[2147483647] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    # 연결된 두 회사
    A, B = map(int, input().split())

    path[A][B] = 1
    path[B][A] = 1

# 자기 자신으로 가는 경로는 0으로 초기화
for i in range(1, N + 1):
    path[i][i] = 0


# 플로이드 워셜 알고리즘
# i: 거쳐가는 회사
# j: 시작 회사
# k: 도착 회사
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            path[j][k] = min(path[j][k], path[j][i] + path[i][k])

# X: 도착해야 하는 회사, K: 거쳐야 하는 회사
X, K = map(int, input().split())

# 도착할 수 없다면 -1 출력
if path[1][K] == 2147483647 or path[K][X] == 2147483647:
    print(-1)
else:
    print(path[1][K] + path[K][X])