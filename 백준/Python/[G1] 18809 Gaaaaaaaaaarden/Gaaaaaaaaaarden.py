from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

# 정원 크기, 초록색 배양액 개수, 빨간색 배양액 개수
N, M, G, R = map(int, input().split())

# 정원
garden = []
# 배양액을 뿌릴 수 있는 칸
possible = []
for i in range(N):
    row = list(map(int, input().split()))
    garden.append(row)
    for j, num in enumerate(row):
        if num == 2:
            possible.append((i, j))

# 피울 수 있는 꽃의 최대 개수
max_cnt = 0

# 배양액을 뿌릴 칸
for pos in combinations(possible, R + G):
    # 초록색 배양액을 뿌릴 칸의 인덱스
    for gi in combinations(range(G + R), G):
        # 정원의 위치별 배양액이 퍼진 시간 (초록: +, 빨강: -, 꽃: 1000)
        time = [[0] * M for _ in range(N)]

        # 꽃의 개수
        cnt = 0

        # 배양액의 위치, 색깔(초록: 1, 빨강: -1), 퍼진 시간을 담은 큐
        q = deque()
        for i in range(G + R):
            r, c = pos[i]
            if i in gi:
                q.append((r, c, 1, 1))
                time[r][c] = 1
            else:
                q.append((r, c, -1, 1))
                time[r][c] = -1

        # BFS로 배양액 퍼뜨리기
        while q:
            # 현재 위치, 배양액 색, 퍼진 시간
            r, c, color, t = q.popleft()

            # 꽃이 있는 곳이라면 패스
            if time[r][c] == 1000:
                continue

            # 사방 탐색
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc

                # 범위 체크
                if not (0 <= nr < N and 0 <= nc < M):
                    continue

                # 다른 색 배양액과 만나는 경우, 꽃 피우기
                if time[nr][nc] + (color * (t + 1)) == 0:
                    time[nr][nc] = 1000
                    cnt += 1
                    continue

                # 이미 다른 배양액이 있는 경우 패스
                if time[nr][nc]:
                    continue

                # 호수가 아니라면 배양액 퍼짐
                if garden[nr][nc] != 0:
                    time[nr][nc] = color * (t + 1)
                    q.append((nr, nc, color, t + 1))

        # 꽃의 개수 비교
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
