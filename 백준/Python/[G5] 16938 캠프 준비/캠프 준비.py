from itertools import combinations
import sys
input = sys.stdin.readline

# 문제 수, 난이도 합 기준, 난이도 차 기준
N, L, R, X = map(int, input().split())

# 문제 난이도 (정렬)
A = sorted(list(map(int, input().split())))

# 주어진 문제가 1개인 경우 불가능
if N == 1:
    print(0)
    exit()

# 문제를 고르는 방법의 수
result = 0

# 고르는 문제 수
for cnt in range(2, N + 1):
    # 문제 고르기
    for questions in combinations(A, cnt):
        # 조건을 만족하는 경우 방법의 수 증가
        if L <= sum(questions) <= R and questions[-1] - questions[0] >= X:
            result += 1

print(result)