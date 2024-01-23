# 테스트케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 배열 크기
    N = int(input())

    # 배열
    nums = [list(map(int, input().split())) for _ in range(N)]

    # 이웃한 요소와의 차이의 합
    s = 0

    # 한 칸씩 탐색
    for i in range(N):
        for j in range(N):
            # 현재 요소
            num = nums[i][j]

            # 오른쪽 요소와 아래쪽 요소만 확인 후 X2
            dr = dd = 0
            if j < N - 1:
                dr = abs(nums[i][j + 1] - num)
            if i < N - 1:
                dd = abs(nums[i + 1][j] - num)

            s += 2 * (dr + dd)

    print(f'#{t} {s}')