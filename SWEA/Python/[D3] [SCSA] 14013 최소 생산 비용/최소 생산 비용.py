# 한 공장씩 제품 선택하기
# idx: 탐색할 공장
# used: 이미 정해진 제품 체크
# cost: 현재까지의 비용
def dfs(idx, used, cost):
    global N, mn

    # 모든 공장을 탐색한 경우 끝내기
    if idx == N:
        mn = min(mn, cost)
        return

    # 현재 최소 비용보다 큰 비용이 나온 경우 패스
    if cost >= mn:
        return

    # 현재 공장이 생산할 제품 선택
    for i in range(N):
        if not used & 1 << i:
            dfs(idx + 1, used | 1 << i, cost + costs[idx][i])

#####################################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 제품 수
    N = int(input())

    # 공장별 생산 비용
    costs = [list(map(int, input().split())) for _ in range(N)]

    # 최소 생산 비용
    mn = 1500

    # 한 공장씩 제품 선택하기
    dfs(0, 0, 0)

    print(f'#{t} {mn}')