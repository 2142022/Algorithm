import sys
input = sys.stdin.readline

# N: 학생 수(=마을의 수), M: 단방향 도로의 개수, X: 파티를 하는 마을
N, M, X = map(int, input().split())

# T[i][j]: i마을에서 j마을까지 가는데 걸리는 시간
# 마을의 번호가 1부터 시작하므로 N+1
T = [[2147483647] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    # s: 출발 마을, d: 도착 마을, t: 걸리는 시간
    s, d, t = map(int, input().split())

    T[s][d] = t

# 플로이드 워셜
# 중간에 지나가는 마을
for k in range(1, N + 1):
    # 출발 마을
    for i in range(1, N + 1):
        # 시간 초과 방지를 위해 T[i][k]가 2147483647인 경우(i마을에서 k마을로 가는 도로가 없는 경우)는 패스
        if T[i][k] == 2147483647:
            continue

        # 도착 마을
        for j in range(1, N + 1):
            # 출발 마을과 도착 마을이 같은 경우
            if i == j:
                T[i][j] = 0
            # 시간 초과 방지를 위해 T[k][j]가 2147483647인 경우(k마을에서 j마을로 가는 도로가 없는 경우)는 패스
            elif T[k][j] == 2147483647:
                continue
            # 최단 거리 비교: 기존 시간과 다른 마을을 지날 때 걸리는 시간 비교
            else:
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])

# 파티에 오고 가는데 가장 오래 걸리는 학생의 소요 시간
result = 0
for i in range(1, N + 1):
    result = max(result, T[i][X] + T[X][i])

print(result)