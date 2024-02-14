import sys
input = sys.stdin.readline

# 현재 범위 내에서 하얀색 색종이 개수, 파란색 색종이 개수 구하기
# (r, c): 탐색 시작점
# n: 탐색 크기
def get_cnt(r, c, n):
    # 탐색하는 범위 내의 합
    s = 0
    for i in range(r, r + n):
        for j in range(c, c + n):
            s += paper[i][j]

    # 하얀색 색종이를 둘 수 있는 경우
    if s == 0:
        return 1, 0
    # 파란색 색종이를 둘 수 있는 경우
    elif s == n * n:
        return 0, 1

    # 색종이를 둘 수 없는 경우 사분할해서 더하기
    nn = n // 2
    x1, y1 = get_cnt(r, c, nn)
    x2, y2 = get_cnt(r, c + nn, nn)
    x3, y3 = get_cnt(r + nn, c, nn)
    x4, y4 = get_cnt(r + nn, c + nn, nn)
    return x1 + x2 + x3 + x4, y1 + y2 + y3 + y4

##################################################################

# 종이 크기
N = int(input())

# 종이
paper = [list(map(int, input().split())) for _ in range(N)]

# 하얀색 색종이 개수, 파란색 색종이 개수
print(*get_cnt(0, 0, N), sep='\n')
