import sys
input = sys.stdin.readline

# 보드 크기
N, M = map(int, input().split())

# 보드
board = [input().rstrip() for _ in range(N)]

# 지민이가 다시 칠해야 하는 정사각형 최소 개수
min_cnt = N * M

# 탐색 시작 위치
for i in range(N - 7):
    for j in range(M - 7):
        # 현재 위치에서 다시 칠해야 하는 정사각형 최소 개수
        # 기준 색깔은 현재 위치의 돌 색깔
        cnt = 0
        color = board[i][j]

        # 8 X 8 탐색
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                # 같은 색이어야 하는 위치에 다른 색이 있는 경우 바꾸기
                if (r + c) % 2 == (i + j) % 2 and board[r][c] != color:
                    cnt += 1
                # 다른 색이어야 하는 위치에 같은 색이 있는 경우 바꾸기
                elif (r + c) % 2 != (i + j) % 2 and board[r][c] == color:
                    cnt += 1

        # 현재 위치 색을 기준으로 하는 경우와, 다른 색을 기준으로 하는 경우 비교
        cnt = min(cnt, 64 - cnt)

        # 최소 횟수 비교
        min_cnt = min(min_cnt, cnt)

print(min_cnt)
