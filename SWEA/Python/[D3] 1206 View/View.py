# 테스트 케이스
for t in range(1, 11):
    # 건물 수
    N = int(input())

    # 건물 높이
    H = list(map(int, input().split()))

    # 조망권이 확보된 세대 수
    cnt = 0

    # 건물 하나씩 탐색
    for i in range(2, N - 2):
        # 왼쪽 2개, 오른쪽 2개 확인
        cnt += min(max(0, H[i] - max(H[i - 1], H[i - 2])), max(0, H[i] - max(H[i + 1], H[i + 2])))

    print(f'#{t} {cnt}')