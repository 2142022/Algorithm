from collections import deque
import sys
input = sys.stdin.readline

# 도화지 크기
n, m = map(int, input().split())

# 도화지
paper = [list(map(int, input().split())) for _ in range(n)]

# 그림 개수
cnt = 0

# 가장 큰 그림의 넓이
max_area = 0

# 그림의 시작점 찾기
for i in range(n):
    for j in range(m):
        if paper[i][j]:
            # 현재 사각형의 넒이
            area = 1
            cnt += 1
            paper[i][j] = 0

            # 탐색 위치를 담은 큐
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()

                # 사방 탐색
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and paper[nr][nc]:
                        area += 1
                        paper[nr][nc] = 0
                        q.append((nr, nc))

            # 그림의 넓이 비교
            max_area = max(max_area, area)

print(cnt)
print(max_area)