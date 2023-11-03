class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # grid의 크기 nxm
        n, m = len(grid), len(grid[0])

        # 사방탐색용
        dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

        # 썩은 오렌지의 위치와 시간 정보를 담은 큐
        q = deque()
        # 오렌지가 있는 곳 체크
        pos = 0
        # 방문 체크
        visited = 0

        for i in range(n):
            for j in range(m):
                # 현재 오렌지
                orange = grid[i][j]

                # 오렌지 위치 체크
                if orange:
                    pos |= 1 << (m * i + j)

                    # 썩은 오렌지 체크
                    if orange == 2:
                        q.append((i, j, 0))
                        visited |= 1 << (m * i + j)

        # 모든 오렌지가 썩을 때까지 걸리는 시간
        time = 0

        # BFS로 썩은 오렌지 탐색
        while visited != pos and q:
            # 현재 위치, 시간
            r, c, t = q.popleft()

            # 사방 탐색
            for d in range(4):
                # 다음 위치
                nr = r + dr[d]
                nc = c + dc[d]

                # 범위를 벗어난 경우 패스 
                if not (0 <= nr < n and 0 <= nc < m):
                    continue

                # 오렌지가 있으면서 방문하지 않은 곳인 경우
                if pos & 1 << (m * nr + nc) and not visited & 1 << (m * nr + nc):
                    # 방문 체크 및 시간 갱신
                    visited |= 1 << (m * nr + nc)
                    time = max(time, t + 1)
                    q.append((nr, nc, t + 1))

        # 모든 오렌지가 썩지 않은 경우 -1
        if pos != visited:
            return -1
        else:
            return time
