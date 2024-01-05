from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 공간의 크기
N = int(input())

# 공간
space = []

# 아기 상어의 위치, 크기
sr, sc, ss = -1, -1, 2
for i in range(N):
    info = list(map(int, input().split()))
    space.append(info)
    if sr == -1:
        for j in range(N):
            if info[j] == 9:
                sr, sc = i, j
                space[i][j] = 0
                break

# 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
time = 0

# 아기 상어가 먹은 물고기의 개수
cnt = 0

# 사방 탐색용 (상, 좌, 우, 하)
dr, dc = (-1, 0, 0, 1), (0, -1, 1, 0)

while True:
    # 물고기를 먹었는지 여부
    eat = 0

    # 방문 체크
    visited = 1 << (N * sr + sc)

    # 이동 시간, 탐색 위치, 탐색 위치에 있는 물고기의 크기를 담은 최소 힙
    h = []
    heappush(h, (0, sr, sc, 0))
    while h:
        # 이동 시간, 탐색 위치, 탐색 위치에 있는 물고기의 크기
        t, r, c, s = heappop(h)

        # 현재 위치의 물고기를 먹는 경우
        if 0 < s < ss:
            space[r][c] = 0
            sr, sc = r, c
            eat = 1
            time += t
            cnt += 1
            if cnt == ss:
                ss += 1
                cnt = 0
            break

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 공간 범위 및 방문 체크
            if not (0 <= nr < N and 0 <= nc < N) or visited & 1 << (N * nr + nc):
                continue
            visited |= 1 << (N * nr + nc)

            # 아기 상어보다 큰 물고기가 아니면 다음 위치 힙에 넣기
            ns = space[nr][nc]
            if ns <= ss:
                heappush(h, (t + 1, nr, nc, ns))

    # 엄마 상어에게 도움을 요청하는 경우
    if not eat:
        print(time)
        break