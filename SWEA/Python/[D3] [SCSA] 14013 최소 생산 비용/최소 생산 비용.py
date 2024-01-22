from heapq import heappush, heappop

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 제품 수
    N = int(input())

    # 공장별 생산 비용
    costs = [list(map(int, input().split())) for _ in range(N)]

    # 방문 체크 (같은 제품의 조합을 탐색하는 경우가 없도록)
    visited = set()

    # 현재까지의 비용, 공장 번호, 선택된 제품을 담은 최소 힙
    h = []
    heappush(h, (0, 0, 0))
    while h:
        # 현재까지의 비용, 공장 번호, 선택된 제품
        cost, idx, selected = heappop(h)

        # 모든 제품이 선택된 경우 끝내기
        if idx == N:
            print(f'#{t} {cost}')
            break

        # 이미 확인한 조합인 경우 패스
        if selected in visited:
            continue
        visited.add(selected)

        # 현재 공장에서의 제품 선택
        for i in range(N):
            # 이미 다른 공장에서 선택한 제품이 아니며, 아직 확인하지 않은 조합 탐색
            if not selected & 1 << i:
                heappush(h, (cost + costs[idx][i], idx + 1, selected | 1 << i))
