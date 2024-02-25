from collections import deque
import sys
input = sys.stdin.readline

# 검은 방을 흰 방으로 바꾼 횟수, 현재 위치, 방문 체크

# 한 줄에 있는 방 수
n = int(input())

# 방들의 정보
rooms = [list(map(int, input().rstrip())) for _ in range(n)]

# 각 방에 도착하기까지 검은 방을 흰 방으로 바꾼 최소 횟수
min_cnt = [[2500] * n for _ in range(n)]
min_cnt[0][0] = 0

# 현재 위치, 검은 방을 흰 방으로 바꾼 횟수, 방문 체크를 담은 큐
q = deque([(0, 0, 0, 1 << 0)])
while q:
    # 현재 위치, 검은 방을 흰 방으로 바꾼 횟수, 방문 체크
    r, c, cnt, visited = q.popleft()

    # 기존 경로보다 방을 바꾼 횟수가 많은 경우 패스
    if min_cnt[r][c] != cnt:
        continue

    # 사방 탐색
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        # 범위 체크
        if not (0 <= nr < n and 0 <= nc < n):
            continue

        # 방문 체크
        if visited & 1 << (n * nr + nc):
            continue

        # 검은 방인 경우
        if rooms[nr][nc] == 0 and min_cnt[nr][nc] > cnt + 1:
            min_cnt[nr][nc] = cnt + 1
            q.append((nr, nc, cnt + 1, visited | 1 << (n * nr + nc)))

        # 흰 방인 경우
        elif rooms[nr][nc] == 1 and min_cnt[nr][nc] > cnt:
            min_cnt[nr][nc] = cnt
            q.append((nr, nc, cnt, visited | 1 << (n * nr + nc)))

print(min_cnt[n - 1][n - 1])