import heapq
import sys
input = sys.stdin.readline

# 최적 혹은 최악의 경로에서의 피로도 반환
# flag: 최적일 때는 -1, 최악일 때는 1
def get_fatigue(flag):
    global N

    # 피로도
    fatigue = 0

    # 방문 체크용
    visited = [0] * (N + 1)
    # 입구 방문체크
    visited[0] = 1

    # 탐색할 도로 정보를 담은 최소 힙
    h = []
    # 입구와 연결된 도로 정보 담기
    heapq.heappush(h, (road[0][0][1] * flag, road[0][0][0]))

    # 최소 힙이 빌 때까지 반복
    while h:
        # A: 현재 건물 번호, C: 도로 종류
        C, A = heapq.heappop(h)

        # 이미 방문한 곳은 패스
        if visited[A]:
            continue

        # 최적의 경로일 경우, C에 -1을 곱해놨으므로 다시 -1 곱하기
        C *= flag
        # 피로도 추가
        if C == 0:
            fatigue += 1

        # 방문 체크
        visited[A] = 1

        # 건물A와 연결된 건물 탐색
        for NA, NC in road[A]:
            # 이미 방문한 건물이라면 넘어가기
            if visited[NA]:
                continue

            # 최소 힙에 담기
            heapq.heappush(h, (NC * flag, NA))

    # 피로도의 제곱 반환
    return fatigue ** 2

##############################################################################################

# N: 건물 개수, M: 도로 개수
N, M = map(int, input().split())

# 도로 정보
# road[1] = [(2, 1), (4, 0)] : 건물1에서 건물2로 가는 길은 내리막길, 건물4로 가는 길은 오르막길
road = [[] for _ in range(N + 1)]
for _ in range(M + 1):
    # A, B: 건물 번호, C: 도로 종류
    A, B, C = map(int, input().split())
    road[A].append((B, C))
    road[B].append((A, C))

# 최악의 경로에서의 피로도 - 최적의 경로에서의 피로도
print(get_fatigue(1) - get_fatigue(-1))
