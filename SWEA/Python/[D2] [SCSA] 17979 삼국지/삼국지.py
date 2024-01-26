# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 나라 수, 국력의 합
    N, M = map(int, input().split())

    # N개의 나라의 국력
    power = list(map(int, input().split()))

    # 세 나라 국력의 합이 M이 되는 경우의 수
    cnt = 0

    # 세 나라 선택
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if power[i] + power[j] + power[k] == M:
                    cnt += 1

    print(f'#{t} {cnt}')