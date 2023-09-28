import sys
input = sys.stdin.readline

# 행렬의 개수
N = int(input())

# 각 행렬의 크기
matrix = [tuple(map(int, input().split())) for _ in range(N)]

# cnt[i][j]: 행렬i부터 행렬j까지 곱하는데 필요한 최소 곱셈 연산 횟수
cnt = [[sys.maxsize] * N for _ in range(N)]
for i in range(N):
    cnt[i][i] = 0

# EX) 행렬 A, B, C, D, E가 있을 때,
# EX) 먼저 AB, BC, CD, CD를 구하고
# EX) 그 후, ABC(A+BC와 AB+C 비교), BCD(B+CD와 BC+D 비교), CDE(C+DE와 CD+E 비교)를 구하고
# EX) 그 후, ABCD(A+BCD, AB+CD, ABC+D 비교), BCDE(B+CDE, BC+DE, BCD+E 비교)를 구하고
# EX) 마지막으로 ABCDE(A+BCDE, AB+CDE, ABC+DE, ABCD+E) 구하기
# 시작 행렬과 마지막 행렬의 인덱스 차이
for i in range(1, N):
    # 시작 행렬의 인덱스
    for j in range(N - i):
        # 곱할 행렬을 두 부분으로 나눌 때, 두 번째 행렬의 인덱스
        for k in range(j + 1, j + i + 1):
            cnt[j][j + i] = min(cnt[j][j + i], cnt[j][k - 1] + cnt[k][j + i] + matrix[j][0] * matrix[k - 1][1] * matrix[j + i][1])

# 모든 행렬을 곱하는데 필요한 최소 곱셈 연산 횟수
print(cnt[0][-1])