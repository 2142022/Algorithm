import sys
input = sys.stdin.readline

# 벨만 포드 알고리즘으로 1번 도시에서 다른 도시까지 가는데 걸리는 최소 시간 구하기
# start: 출발 도시
def bellmanford(start):
    # 출발 도시는 0으로 갱신
    time[start] = 0

    # 노선 정보를 N번 탐색
    for i in range(N):
        # 모든 노선 정보 탐색
        for s, d, e in edges:
            # 기존 시간보다 적게 걸린다면 갱신
            # 출발 노드가 1번 이상 갱신되었는지 확인해야 함
            # 출발 노드인 s까지 가는 경로가 없는데 e가 음수라면 갱신되기 때문
            if time[s] != 2147483647 and time[s] + e < time[d]:
                time[d] = time[s] + e

                # 만약 N번째 탐색 시까지 갱신이 된다면 시간이 계속 줄어들고 있음을 의미
                # 즉, 시간을 무한히 오래 전으로 되돌릴 수 있으므로 -1 출력
                if i == N - 1:
                    return False

    return True

#####################################################################################

# N: 도시의 개수, M: 버스 노선의 개수
N, M = map(int, input().split())

# 노선 정보
edges = [list(map(int, input().split())) for _ in range(M)]

# 1번 도시에서부터 다른 도시까지 가는데 걸리는 최소 시간
time = [2147483647] * (N + 1)

# 어떤 도시로 갈 때 무한히 오래 전으로 되돌릴 수 있다면 -1 출력
if not bellmanford(1):
    print(-1)
# 각 도시까지 가는데 걸리는 최소 시간 출력
else:
    for i in range(2, N + 1):
        # 가는 경로가 없는 경우 -1 출력
        if time[i] == 2147483647:
            print(-1)
        else:
            print(time[i])