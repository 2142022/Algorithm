import sys
input = sys.stdin.readline

# 테스트케이스 개수
T = int(input())
for _ in range(T):
    # 소설을 구성하는 장(chapter) 수
    K = int(input())

    # 각 파일의 크기
    # 인덱스 범위를 벗어나지 않도록 앞에 [0] 추가
    files = [0] + list(map(int, input().split()))

    # 파일 0부터 파일 i까지의 파일 크기 합
    total = [0] * (K + 1)
    for i in range(1, K + 1):
        total[i] = total[i - 1] + files[i]

    # cost[i][j]: 파일 i부터 파일 j까지 합치는데 필요한 최소 비용
    cost = [[0] * (K + 1) for _ in range(K + 2)]

    # idx[i][j]: 파일 i부터 파일 j까지를 하나로 합치기 전, 두 임시파일을 나누는 최적의 위치
    # 즉, cost[i][j]가 최소 비용이 되도록 하는 파일의 인덱스
    idx = [[0] * (K + 1) for _ in range(K + 1)]
    for i in range(1, K + 1):
        idx[i][i] = i

    # cnt: 합칠 파일의 총 개수
    for cnt in range(2, K + 1):
        # start: 합칠 파일의 시작 파일
        for start in range(1, K - cnt + 2):
            end = start + cnt - 1
            cost[start][end] = sys.maxsize

            # i: 합칠 파일들을 두 부분으로 나누는 위치
            for i in range(idx[start][end - 1], idx[start + 1][end] + 1):
                # 현재 위치에서 두 임시파일을 합쳤을 경우의 비용
                c = cost[start][i] + cost[i + 1][end] + total[end] - total[start - 1]
                if c < cost[start][end]:
                    cost[start][end] = c
                    idx[start][end] = i

    # 모든 장을 합치는데 필요한 최소 비용
    print(cost[1][K])

