# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 유적지 크기, 외계인 수, 찾을 색깔
    N, K, C = map(int, input().split())

    # 유적지
    board = [[0] * N for _ in range(N)]

    # 발자국 찍기
    for _ in range(K):
        # 행, 열, 높이, 너비, 색깔
        i, j, h, w, c = map(int, input().split())

        # 한 행에 찍을 발자국
        row = [c] * w
        for k in range(i, i + h):
            board[k][j:j + w] = row

    # 원하는 색깔의 넓이 구하기
    area = 0
    for i in range(N):
        area += board[i].count(C)

    print(f'#{t} {area}')