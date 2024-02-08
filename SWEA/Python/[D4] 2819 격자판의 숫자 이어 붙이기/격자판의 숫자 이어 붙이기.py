# 한 칸씩 탐색
def dfs(r, c, num):
    # 일곱 자리가 된 경우 끝내기
    if len(num) == 7:
        nums.add(num)
        return

    # 사방 탐색
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, num + board[nr][nc])

#############################################################################

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 격자판
    board = [input().replace(' ', '') for _ in range(4)]

    # 만들 수 있는 모든 수
    nums = set()

    # 시작점
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j])

    # 가능한 수들의 개수 출력
    print(f'#{t} {len(nums)}')