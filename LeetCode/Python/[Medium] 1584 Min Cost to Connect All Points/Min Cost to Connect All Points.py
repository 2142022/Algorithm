import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 점 개수
        N = len(points)

        # 점들 사이의 거리
        # distance[0] = [(3, 1), (2, 2)] 
        # : 0번째 점은 1번째 점과의 거리가 3, 2번째 점과의 거리가 2임을 의미
        distance = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    d = abs(x1 - x2) + abs(y1 - y2)

                    distance[i].append((d, j))
                    distance[j].append((d, i))

        # 모든 점들을 연결했을 때의 최소 거리
        min_distance = 0

        # 방문 체크용
        visited = [0] * N

        # 연결한 점의 개수
        cnt = 0

        # 연결할 수 있는 점과 거리 정보를 담은 최소 힙
        h = []
        heapq.heappush(h, (0, 0))

        # 모든 점들이 연결될 때까지 반복
        while cnt != N:
            # 현재 연결할 수 있는 점들 중 가장 짧은 거리와 점의 인덱스
            d, i = heapq.heappop(h)

            # 이미 방문한 점은 패스
            if visited[i]:
                continue

            # 방문체크
            visited[i] = 1
            cnt += 1
            min_distance += d

            # 다음으로 연결할 수 있는 점들 힙에 넣기
            for nd, ni in distance[i]:
                # 아직 방문하지 않은 점들만 넣기
                if not visited[ni]:
                    heapq.heappush(h, (nd, ni))

        # 모든 점을 연결할 수 있는 최소 거리 반환
        return min_distance
                