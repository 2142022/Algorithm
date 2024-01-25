# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 깃발 크기
    N, M = map(int, input().split())

    # 각 색에 대응하는 숫자
    color = {'W': 0, 'B': 1, 'R': 2}

    # cnt[i][j]: i행을 j색으로 바꾸기 위해 바꿔야 하는 칸 수
    change = [[0] * 3 for _ in range(N)]
    for i in range(N):
        info = input().rstrip()
        for c in color:
            change[i][color[c]] = M - info.count(c)

    # 새로 칠해야 하는 최소 칸 수
    mn_cnt = N * M

    # 흰 색의 마지막 줄
    for i in range(N - 2):
        # 새로 칠해야 하는 칸 수
        cnt = sum(list(zip(*change[:i + 1]))[0])

        # 파란색의 마지막 줄
        for j in range(i + 1, N - 1):
            # 파란색 + 빨간색
            cnt += sum(list(zip(*change[i + 1:j + 1]))[1]) + sum(list(zip(*change[j + 1:]))[2])

            # 바꿔야 하는 최소 칸 수와 비교
            mn_cnt = min(mn_cnt, cnt)

    print(f'#{t} {mn_cnt}')