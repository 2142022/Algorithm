import sys
input = sys.stdin.readline

# 연속해서 4개 지점 선택하기
# s: 현재까지 선택한 숫자의 합
def get_sum(s):
    global max_sum

    # 4개의 수가 정해진 경우, 최댓값 비교
    if len(pos) == 4:
        max_sum = max(max_sum, s)
        return

    # 나머지 모든 수를 더해도 최댓값을 넘지 못하는 경우 끝내기
    if s + max_num * (4 - len(pos)) <= max_sum:
        return

    # 방문한 곳
    for r, c in pos:
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue

            # 다음 위치 탐색
            pos.append((nr, nc))
            visited[nr][nc] = 1
            get_sum(s + board[nr][nc])
            visited[nr][nc] = 0
            pos.pop()

############################################################################

# 종이 크기
N, M = map(int, input().split())

# 종이에 쓰여 있는 수
board = []
# 종이 위의 최대 숫자
max_num = 0
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    max_num = max(max_num, max(row))

# 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값
max_sum = 0

# 방문한 위치
pos = []
# 방문 체크
visited = [[0] * M for _ in range(N)]

# 주어진 테트로미노는 4개를 연속해서 만들 수 있는 모든 모양
# -> 연속한 4개의 숫자의 최대 합 구하기
for i in range(N):
    for j in range(M):
        # 현재 지점에서 연속적으로 4개를 선택했을 때 최대 합 구하기
        pos.append((i, j))
        visited[i][j] = 1
        get_sum(board[i][j])
        pos.pop()
        visited[i][j] = 0

print(max_sum)