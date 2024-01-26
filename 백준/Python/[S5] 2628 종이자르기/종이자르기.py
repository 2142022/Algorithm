from bisect import bisect_left
import sys
input = sys.stdin.readline

# 가로, 세로 길이
N, M = map(int, input().split())

# 잘리는 열 번호, 잘리는 행 번호
col, row = [0, N], [0, M]

# 자르는 횟수
C = int(input())
for _ in range(C):
    # 자르는 방향, 번호
    d, i = map(int, input().split())

    # 가로로 자르기
    if d == 0:
        row.insert(bisect_left(row, i), i)

    # 세로로 자르기
    else:
        col.insert(bisect_left(col, i), i)

# 가장 큰 넓이
area = 0
for i in range(1, len(row)):
    # 세로 길이
    h = row[i] - row[i - 1]

    for j in range(1, len(col)):
        # 가로 길이
        w = col[j] - col[j - 1]

        # 넓이 비교
        area = max(area, h * w)

print(area)