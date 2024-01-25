from collections import deque
import sys
input = sys.stdin.readline

# JOI시 크기
H, W = map(int, input().split())

# 구름이 뜨는 시간
time = [[-1] * W for _ in range(H)]
# 구름 위치 및 구름이 뜨는데 걸린 시간을 담은 큐
q = deque()
for i in range(H):
    info = input().rstrip()
    for j in range(W):
        if info[j] == 'c':
            time[i][j] = 0
            q.append((i, j, 0))

# BFS
while q:
    # 구름 위치 및 구름이 뜨는데 걸린 시간
    r, c, t = q.popleft()

    # 오른쪽으로 이동
    c += 1

    # 범위 내의 위치라면 큐에 담기
    if c < W and time[r][c] == -1:
        time[r][c] = t + 1
        q.append((r, c, t + 1))

for t in time:
    print(*t)