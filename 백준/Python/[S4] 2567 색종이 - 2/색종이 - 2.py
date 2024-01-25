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

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 색종이 둘레
length = 0
for i in range(100):
    for j in range(100):
        if not paper[i][j]:
            continue

        # 현재 위치에서 사방의 색종이 개수 세기
        cnt = 0
        for d in range(4):
            ni, nj = i + dr[d], j + dc[d]
            if 0 <= ni < 100 and 0 <= nj < 100 and paper[ni][nj]:
                cnt += 1

        # 꼭짓점에 있는 곳은 길이를 2번 더해줌
        if cnt == 2:
            length += 2
        # 모서리
        elif cnt == 3:
            length += 1

print(length)