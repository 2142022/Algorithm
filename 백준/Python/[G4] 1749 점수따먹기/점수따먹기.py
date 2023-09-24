import sys
input = sys.stdin.readline

# (N + 1) X (M + 1) 행렬
# 첫 행과 첫 열은 모두 0으로 채우기
N, M = map(int, input().split())
matrix = [[0] * (M + 1)] + [([0] + list(map(int, input().split()))) for _ in range(N)]

# 부분행렬의 원소 합의 최대값
result = -400000000

# 시작 행
for i in range(1, N + 1):
    # 각 열별 누적합
    col = [0] * (M + 1)

    # 끝 행
    for j in range(i, N + 1):
        # i행부터 j행까지 모두 사용했을 때, 만들 수 있는 사각형 중 누적합의 최대값
        row = [0] * (M + 1)

        # 열 탐색
        for k in range(1, M + 1):
            col[k] += matrix[j][k]
            row[k] = max(row[k - 1] + col[k], col[k])
            result = max(result, row[k])

print(result)