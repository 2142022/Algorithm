from collections import deque

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 1일, 1달, 3달, 1년 이용권 요금
    day, month, month3, year = map(int, input().split())

    # 월별 이용 계획
    plan = list(map(int, input().split()))

    # 최소 비용
    min_cost = year

    # 현재 월, 현재까지의 비용을 담은 큐
    q = deque([(0, day * plan[0]), (0, month), (2, month3)])
    while q:
        # 현재 월, 현재까지의 비용
        n, cost = q.popleft()

        # 12월인 경우, 최소 비용 비교
        if n >= 11:
            min_cost = min(min_cost, cost)
            continue

        # 다음 이용 계획 큐에 추가
        if cost + day * plan[n + 1] < min_cost:
            q.append((n + 1, cost + day * plan[n + 1]))
        if cost + month < min_cost:
            q.append((n + 1, cost + month))
        if cost + month3 < min_cost:
            q.append((n + 3, cost + month3))

    print(f'#{t} {min_cost}')
