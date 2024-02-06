import sys
input = sys.stdin.readline

# 보드 크기
R, C = map(int, input().split())

# 보드
board = [list(map(lambda x: ord(x) - ord('A'), input().rstrip())) for _ in range(R)]

# 말이 지날 수 있는 최대 칸 수
max_cnt = 0

# 탐색 위치, 사용 알파벳, 지나간 칸 수를 담은 스택
stack = [(0, 0, 1 << board[0][0], 1)]
while stack:
    # 탐색 위치, 사용 알파벳, 지나간 칸 수
    r, c, used, cnt = stack.pop()
    max_cnt = max(max_cnt, cnt)

    # 모든 알파벳이 다 나온 경우 패스
    if max_cnt == 26:
        break

    # 사방 탐색
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and not used & 1 << board[nr][nc]:
            stack.append((nr, nc, used | 1 << board[nr][nc], cnt + 1))

print(max_cnt)