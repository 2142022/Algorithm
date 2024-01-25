import sys
input = sys.stdin.readline

# 평면
board = [[-1] * 1001 for _ in range(1001)]

# 색종이 종류 수
N = int(input())

# 색종이별 숫자로 저장
for num in range(N):
    # 왼쪽 상단 위치, 너비, 높이
    # 주어진 값은 왼쪽 하단이지만, 평면도 위아래 바껴서 주어지므로 반대로 생각하기
    c, r, w, h = map(int, input().split())

    # 색종이의 한 행
    row = [num] * w

    # 평면 위에 색종이 체크
    for i in range(r, r + h):
        board[i][c : c + w] = row

# 각 색종이 개수
cnt = [0] * N
for b in board:
    for num in range(N):
        cnt[num] += b.count(num)

for i in cnt:
    print(i)