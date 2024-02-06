from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 모눈종이 크기
N, M = map(int, input().split())

# 모눈종이
paper = [list(map(int, input().split())) for _ in range(N)]

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 치즈 외부 공간을 담은 큐
q = deque([(0, 0)])
paper[0][0] = 2

# 치즈 위치와 치즈 외부 공기와 접촉한 면의 개수를 담은 딕셔너리
cnt = defaultdict(int)

# 치즈가 녹는데 걸리는 시간
time = 0

# 치즈가 없는 칸의 개수 ((0, 0)은 이미 외부 공간으로 체크했으므로 -1)
empty = N * M - 1
while True:
    # 치즈 외부 공간은 모두 2로 바꾸기
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if paper[nr][nc] == 0:
                    paper[nr][nc] = 2
                    empty -= 1
                    q.append((nr, nc))
                # 치즈인 경우 외부 접촉면 개수 증가
                elif paper[nr][nc] == 1:
                    cnt[(nr, nc)] += 1

    # 치즈가 모두 녹은 경우 끝내기
    if empty == 0:
        print(time)
        break

    # 공기와 접촉한 면이 2개 이상인 치즈 녹이기
    for r, c in [k for k, v in cnt.items() if v >= 2 and paper[k[0]][k[1]] == 1]:
        empty -= 1
        paper[r][c] = 2
        q.append((r, c))
        cnt.pop((r, c))

    # 시간 증가
    time += 1