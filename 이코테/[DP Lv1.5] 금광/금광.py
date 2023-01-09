import sys
input = sys.stdin.readline

# 테스트케이스 개수
T = int(input())

for t in range(T):
    # n x m 행렬: 각 칸의 금의 크기
    n, m = map(int, input().split())

    # n x m개의 위치에 매장된 금의 개수
    gold = list(map(int, input().split()))

    # 각 행별 금의 최대 크기
    value = [[0] * m for _ in range(n)]
    # 1열의 금의 크기로 초기화
    for i in range(n):
        value[i][0] = gold[i * m]

    # m - 1번 반복 (1열은 초기화했으므로 제외)
    for j in range(1, m):
        # 현재 금의 크기에서 왼쪽 위, 왼쪽, 왼쪽 아래 중 가장 큰 값 더하기
        for i in range(n):
            if i == 0:
                value[i][j] = gold[i * m + j] + max(value[i][j - 1], value[i + 1][j - 1])
            elif i == n - 1:
                value[i][j] = gold[i * m + j] + max(value[i - 1][j - 1], value[i][j - 1])
            else:
                value[i][j] = gold[i * m + j] + max(value[i - 1][j - 1], value[i][j - 1], value[i + 1][j - 1])

    # 마지막 열에서 최대값 찾기
    max_value = 0
    for i in range(n):
        max_value = max(max_value, value[i][m - 1])

    print(max_value)