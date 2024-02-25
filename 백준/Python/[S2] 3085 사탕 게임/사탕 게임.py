import sys
input = sys.stdin.readline

# 기준 사탕 기준 왼쪽으로 연속된 사탕의 개수
# color: 기준 사탕의 색
# change: 사탕을 바꾼 여부
def left(color, change):
    cnt = 1
    while j - cnt >= 0 and board[i][j - cnt] == color:
        if not change:
            visited[i][j - cnt] = 1
        cnt += 1
    return cnt - 1

###########################################################################################

# 기준 사탕 기준 오른쪽으로 연속된 사탕의 개수
# color: 기준 사탕의 색
# change: 사탕을 바꾼 여부
def right(color, change):
    cnt = 1
    while j + cnt < N and board[i][j + cnt] == color:
        if not change:
            visited[i][j + cnt] = 1
        cnt += 1
    return cnt - 1

###########################################################################################

# 기준 사탕 기준 위쪽으로 연속된 사탕의 개수
# color: 기준 사탕의 색
# change: 사탕을 바꾼 여부
def up(color, change):
    cnt = 1
    while i - cnt >= 0 and board[i - cnt][j] == color:
        if not change:
            visited[i - cnt][j] = 1
        cnt += 1
    return cnt - 1

###########################################################################################

# 기준 사탕 기준 아래쪽으로 연속된 사탕의 개수
# color: 기준 사탕의 색
# change: 사탕을 바꾼 여부
def down(color, change):
    cnt = 1
    while i + cnt < N and board[i + cnt][j] == color:
        if not change:
            visited[i + cnt][j] = 1
        cnt += 1
    return cnt - 1

###########################################################################################

# 보드 크기
N = int(input())

# 보드
board = [input().rstrip() for _ in range(N)]

# 먹을 수 있는 최대 사탕 개수
max_cnt = 0

# 원래 보드에서의 방문 체크
visited = [[0] * N for _ in range(N)]

# 사탕을 바꿀 위치
for i in range(N):
    for j in range(N):
        # 현재 위치의 사탕
        color = board[i][j]

        # 사탕을 바꾸지 않는 경우
        if not visited[i][j]:
            visited[i][j] = 1

            # 가로
            max_cnt = max(max_cnt, left(color, 0) + right(color, 0) + 1)

            # 세로
            max_cnt = max(max_cnt, up(color, 0) + down(color, 0) + 1)

        # 위 사탕과 바꾸는 경우
        if i - 1 >= 0 and board[i - 1][j] != color:
            # 바꾼 사탕
            change = board[i - 1][j]
            max_cnt = max(max_cnt, left(change, 1) + right(change, 1) + 1)
            max_cnt = max(max_cnt, down(change, 1) + 1)

        # 아래 사탕과 바꾸는 경우
        if i + 1 < N and board[i + 1][j] != color:
            # 위 사탕과 다른 경우만 탐색
            if i - 1 < 0 or (i - 1 >= 0 and board[i + 1][j] != board[i - 1][j]):
                # 바꾼 사탕
                change = board[i + 1][j]
                max_cnt = max(max_cnt, left(change, 1) + right(change, 1) + 1)
                max_cnt = max(max_cnt, up(change, 1) + 1)

        # 왼쪽 사탕과 바꾸는 경우
        if j - 1 >= 0 and board[i][j - 1] != color:
            # 바꾼 사탕
            change = board[i][j - 1]
            max_cnt = max(max_cnt, up(change, 1) + down(change, 1) + 1)
            max_cnt = max(max_cnt, right(change, 1) + 1)

        # 오른쪽 사탕과 바꾸는 경우
        if j + 1 < N and board[i][j + 1] != color:
            # 왼쪽 사탕과 다른 경우만 탐색
            if j - 1 < 0 or (j - 1 >= 0 and board[i][j + 1] != board[i][j - 1]):
                # 바꾼 사탕
                change = board[i][j + 1]
                max_cnt = max(max_cnt, up(change, 1) + down(change, 1) + 1)
                max_cnt = max(max_cnt, left(change, 1) + 1)

print(max_cnt)