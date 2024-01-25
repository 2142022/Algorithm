# 10개의 테스트케이스
for _ in range(10):
    # 테스트케이스 번호
    t = int(input())

    # 사다리
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 현재 위치 (처음에는 도착 지점으로 지정), 이동 방향
    r, c, d = 99, ladder[99].index(2), 0

    # 상, 좌, 우 탐색용
    dr, dc = (-1, 0, 0), (0, -1, 1)

    # 출발점에 도착할 때까지 탐색
    while True:
        # 한 칸 이동
        r += dr[d]
        c += dc[d]

        # 출발점에 도착한 경우 끝내기
        if r == 0:
            break

        # 위쪽으로 이동할 때는 왼쪽이나 오른쪽에 사다리가 있는지 확인
        # 왼쪽으로 이동할 때는 위로 가는 사다리가 있는지 확인
        # 오른쪽으로 이동할 때는 위로 가는 사다리가 있는지 확인
        if d == 0:
            if c - 1 >= 0 and ladder[r][c - 1]:
                d = 1
            elif c + 1 < 100 and ladder[r][c + 1]:
                d = 2
        elif r - 1 >= 0 and ladder[r - 1][c]:
            d = 0

    print(f'#{t} {c}')