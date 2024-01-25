import sys
input = sys.stdin.readline

# 색종이 수
N = int(input())

# 색종이가 있는 곳 체크
paper = [[0] * 100 for _ in range(100)]

# 색종이의 한 행
row = [1] * 10

# 색종이 체크
for _ in range(N):
    # 색종이 시작 위치
    c, r = map(int, input().split())
    for i in range(r, r + 10):
        paper[i][c:c+10] = row

# 색종이 넓이
cnt = 0
for p in paper:
    cnt += p.count(1)

print(cnt)