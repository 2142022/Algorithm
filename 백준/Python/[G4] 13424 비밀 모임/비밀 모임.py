from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 친구들의 이동 거리의 최소 합 구하기
# x: 모이는 위치
def dijkstra(x):
    # x로부터 다른 곳까지의 거리
    d = [sys.maxsize] * (N + 1)
    d[x] = 0

    # 탐색 위치와 거리를 담은 큐
    q = deque([(x, 0)])
    while q:
        # 현재 위치와 현재까지의 거리
        p, l = q.popleft()

        # 기존 거리보다 큰 경우 패스
        if l > d[p]:
            continue

        # 연결된 곳 탐색
        for np, nl in connect[p]:
            # 기존 거리보다 작은 경우 큐에 담기
            if l + nl < d[np]:
                d[np] = l + nl
                q.append((np, l + nl))

    # 친구들의 이동거리의 최소 합 반환
    result = 0
    for i in friends:
        result += d[i]

    return result

##################################################

# 테스트케이스 수
T = int(input())
for _ in range(T):
    # 방의 개수, 비밀통로의 개수
    N, M = map(int, input().split())

    # 비밀 통로 정보
    connect = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        connect[a].append((b, c))
        connect[b].append((a, c))

    # 친구 수
    K = int(input())

    # 친구들의 위치
    friends = list(map(int, input().split()))

    # 최소 거리
    dist = sys.maxsize
    # 최소 거리일 때 모이는 방 번호
    room = 0

    # 모이는 위치
    for i in range(1, N + 1):
        # 최소 거리 비교
        d = dijkstra(i)
        if d < dist:
            dist = d
            room = i

    print(room)