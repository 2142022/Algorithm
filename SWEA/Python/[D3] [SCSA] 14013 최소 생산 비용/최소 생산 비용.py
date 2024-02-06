# i번째 제품의 공장 고르기
# cost: 현재까지의 비용
def dfs(i, cost):
    global N, min_cost

    # 모든 공장을 선택한 경우 최소 생산 비용 비교
    if i == N:
        min_cost = min(min_cost, cost)
        return

    # 현재 제품에 대한 공장 선택
    for j in range(N):
        if not visited[j] and cost + V[i][j] < min_cost:
            visited[j] = 1
            dfs(i + 1, cost + V[i][j])
            visited[j] = 0

#################################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 제품 수
    N = int(input())

    # 공장별 생산 비용
    V = [list(map(int, input().split())) for _ in range(N)]

    # 선택한 공장 체크
    visited = [0] * N

    # 최소 생산 비용
    min_cost = 99 * N

    # 한 제품씩 공장 고르기
    dfs(0, 0)

    print(f'#{t} {min_cost}')