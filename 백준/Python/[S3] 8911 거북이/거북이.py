import sys
input = sys.stdin.readline

# 경계값 비교
def update():
    global up, down, left, right

    if r > up:
        up = r

    if r < down:
        down = r

    if c < left:
        left = c

    if c > right:
        right = c

#######################################################

# 사방 탐색용
dr, dc = (1, 0, -1, 0), (0, 1, 0, -1)

# 테스트 케이스
for _ in range(int(input())):
    # 거북이가 만드는 직사각형 경계 위치
    up, down, left, right = 0, 0, 0, 0

    # 거북이 위치, 방향
    r, c, d = 0, 0, 0

    # 컨트롤 프로그램
    for op in input().rstrip():
        # 앞으로 이동
        if op == 'F':
            r += dr[d]
            c += dc[d]

            # 경계 비교
            update()

        # 뒤로 이동
        elif op == 'B':
            r += dr[(d + 2) % 4]
            c += dc[(d + 2) % 4]

            # 경계 비교
            update()

        # 왼쪽으로 90도 회전
        elif op == 'L':
            d = (d - 1) % 4

        # 오른쪽으로 90도 회전
        else:
            d = (d + 1) % 4

    # 거북이가 이동한 영역을 모두 포함하는 가장 작은 직사각형의 넓이
    print((up - down) * (right - left))