# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 정수 개수, 구간 개수
    N, M = map(int, input().split())

    # N개의 정수
    a = list(map(int, input().split()))

    # 탐색하는 구간의 합
    s = 0
    for i in range(M):
        s += a[i]

    # 최대 구간합, 최소 구간합
    mx = mn = s

    # 구간을 한 칸씩 옮겨가며 탐색
    for i in range(M, N):
        # 구간합 갱신
        s += a[i] - a[i - M]

        # 구간합 비교
        mx = max(mx, s)
        mn = min(mn, s)

    # 최대 구간합 - 최소 구간합
    print(f'#{t} {mx - mn}')