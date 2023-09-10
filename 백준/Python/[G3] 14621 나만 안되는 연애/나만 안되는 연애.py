import sys, heapq
input = sys.stdin.readline

# N: 학교 수, M: 도로 수
N, M = map(int, input().split())

# 각 학교의 성별
sex = [''] + list(input().rstrip().split())

# 모든 도로 정보
road = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    road[u].append((d, v))
    road[v].append((d, u))

# 최종 경로의 길이
l = 0
# 연결한 학교 수
cnt = 0
# 방문 체크
visited = [0] * (N + 1)
# 탐색할 도로 정보를 담은 최소 힙
h = []
heapq.heappush(h, (0, 1))

# 학교 연결하기
while h:
    # 현재까지 연결한 경로의 길이, 현재 학교
    d, i = heapq.heappop(h)

    # 이미 방문한 곳은 패스
    if visited[i]:
        continue

    # 현재 학교 연결
    visited[i] = 1
    cnt += 1
    l += d

    # 모든 학교를 연결했으면 끝내기
    if cnt == N:
        break

    # 다음 학교 탐색
    for nd, ni in road[i]:
        # 다음 학교의 성별이 같거나 이미 방문한 곳은 패스
        if sex[ni] == sex[i] or visited[ni]:
            continue

        # 다음 학교 큐에 추가
        heapq.heappush(h, (nd, ni))

# 결과 출력
if cnt == N:
    print(l)
else:
    print(-1)
