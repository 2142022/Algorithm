import sys
input = sys.stdin.readline

# 방문 체크
visited = [[0] * 6 for _ in range(6)]

# 출발 지점
pos = input().rstrip()
sr, sc = 6 - int(pos[1]), ord(pos[0]) - ord('A')
visited[sr][sc] = 1

# 투어 중 이전 위치
pr, pc = sr, sc

# 나이트 투어
for _ in range(35):
    # 위치
    pos = input().rstrip()
    r, c = 6 - int(pos[1]), ord(pos[0]) - ord('A')

    # 방문 체크
    if visited[r][c]:
        print('Invalid')
        exit()
    visited[r][c] = 1

    # 이전 위치에서 현재 위치로 올 수 있는지 확인
    if not (abs(pr - r) and abs(pc - c) and abs(pr - r) + abs(pc - c) == 3):
        print('Invalid')
        exit()

    pr, pc = r, c

# 시작점으로 돌아올 수 있는지 확인
if abs(pr - sr) and abs(pc - sc) and abs(pr - sr) + abs(pc - sc) == 3:
    print('Valid')
else:
    print('Invalid')