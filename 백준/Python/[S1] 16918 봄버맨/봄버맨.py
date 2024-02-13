from collections import deque
import sys
input = sys.stdin.readline

# 격자판 크기, 격자판 상태를 알고 싶은 시간
R, C, N = map(int, input().split())

# 격자판 (폭탄이 없는 칸은 -1, 폭탄이 있는 칸은 폭탄이 설치된 시간 저장)
grid = [list(map(lambda x: -1 if x == '.' else 0, input().rstrip())) for _ in range(R)]

# 짝수초에는 항상 폭탄이 채워져 있음
if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
    exit()

# 시간
t = 2

# N초까지 반복
while t <= N:
    # 짝수초에는 폭탄 채우기
    if t % 2 == 0:
        for i in range(R):
            for j in range(C):
                if grid[i][j] == -1:
                    grid[i][j] = t

    # 홀수초에는 3초전에 채운 폭탄 폭발
    else:
        # 3초 전에 채운 폭탄의 위치를 담은 큐
        q = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == t - 3:
                    grid[i][j] = -1
                    q.append((i, j))

        # 폭탄의 사방에 있는 폭탄 없애기
        while q:
            r, c = q.popleft()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    grid[nr][nc] = -1

    t += 1

# 원하는 시간의 격자판 상태 출력
for row in grid:
    print(''.join(list(map(lambda x: '.' if x == -1 else 'O', row))))