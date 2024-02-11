import sys
input = sys.stdin.readline

# 색종이 개수 구하기
# r, c: 현재 종이 시작점
# n: 현재 종이 크기
def dfs(r, c, n):
    # 현재 종이의 숫자의 합
    s = 0
    for i in range(r, r + n):
        for j in range(c, c + n):
            s += paper[i][j]

    # 현재 종이가 하얀색 색종이인 경우
    if s == 0:
        return 1, 0

    # 현재 종이가 파란색 색종이인 경우
    if s == n * n:
        return 0, 1

    # 더 나눠야 하는 경우
    nn = n // 2
    x1, y1 = dfs(r, c, nn)
    x2, y2 = dfs(r, c + nn, nn)
    x3, y3 = dfs(r + nn, c, nn)
    x4, y4 = dfs(r + nn, c + nn, nn)
    return x1 + x2 + x3 + x4, y1 + y2 + y3 + y4

################################################################

# 전체 종이 크기
N = int(input())

# 전체 종이
paper = [list(map(int, input().split())) for _ in range(N)]

# 색종이 개수
cnt = dfs(0, 0, N)
print(cnt[0])
print(cnt[1])