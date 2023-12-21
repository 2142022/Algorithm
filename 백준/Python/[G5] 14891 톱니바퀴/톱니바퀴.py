from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 4개 톱니바퀴의 상태
gear = defaultdict(list)
for i in range(1, 5):
    gear[i] = list(map(int, input().rstrip()))

# 각 톱니바퀴에서 12시 방향을 가리키는 톱니
idx = defaultdict(int)
idx[1] = idx[2] = idx[3] = idx[4] = 0

# 회전 횟수
K = int(input())

# 회전
for _ in range(K):
    # 회전시킬 톱니바퀴, 회전 방향
    r, d = map(int, input().split())

    # 방문체크
    visited = 1 << r

    # 회전 시킬 톱니바퀴와 회전 방향
    rotate = [(r, d)]

    # 탐색할 톱니바퀴와 회전 방향을 담은 큐
    q = deque([(r, d)])
    while q:
        # 현재 톱니바퀴, 회전 방향
        r, d = q.popleft()

        # 왼쪽 톱니바퀴 탐색
        if r != 1 and not visited & 1 << (r - 1) and gear[r][(idx[r] + 6) % 8] != gear[r - 1][(idx[r - 1] + 2) % 8]:
            rotate.append((r - 1, -d))
            q.append((r - 1, -d))
            visited |= 1 << (r - 1)

        # 오른쪽 톱니바퀴 탐색
        if r != 4 and not visited & 1 << (r + 1) and gear[r][(idx[r] + 2) % 8] != gear[r + 1][(idx[r + 1] + 6) % 8]:
            rotate.append((r + 1, -d))
            q.append((r + 1, -d))
            visited |= 1 << (r + 1)

    # 회전시킬 톱니바퀴 모두 회전
    for r, d in rotate:
        idx[r] = (idx[r] - d) % 8

# 최종 점수 구하기
score = 0
for i in range(1, 5):
    if gear[i][idx[i]]:
        score += 2 ** (i - 1)

print(score)
