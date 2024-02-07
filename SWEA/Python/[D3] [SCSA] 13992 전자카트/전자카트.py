# 하나씩 방문
# i: 현재 위치
# cnt: 이동한 횟수
# cost: 현재까지의 배터리 소비
def go(i, cnt, cost):
    global min_cost

    # 최소 소비량 이상인 경우 끝내기
    if cost >= min_cost:
        return

    # 더 이상 최소 소비량이 더 낮아질 수 없는 경우 끝내기
    if min_cost == 1 * N:
        return

    # 모든 구역을 방문한 경우, 최소 소비량 비교
    if cnt == N - 1:
        cost += battery[i][0]
        min_cost = min(min_cost, cost)
        return

    # 다음 위치 정하기
    for j in range(1, N):
        if not visited[j]:
            visited[j] = 1
            go(j, cnt + 1, cost + battery[i][j])
            visited[j] = 0

############################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 관리구역 수
    N = int(input())

    # 배터리 소비량
    battery = [list(map(int, input().split())) for _ in range(N)]

    # 최소 배터리 소비량
    min_cost = 100 * N

    # 방문 체크
    visited = [0] * N
    visited[0] = 1

    # 하나씩 방문
    go(0, 0, 0)

    print(f'#{t} {min_cost}')