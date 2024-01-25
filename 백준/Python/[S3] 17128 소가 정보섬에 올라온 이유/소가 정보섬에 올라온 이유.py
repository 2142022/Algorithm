import sys
input = sys.stdin.readline

# 소의 수, 장난칠 횟수
N, M = map(int, input().split())

# 소들의 품질 점수
A = list(map(int, input().split()))

# i번째 소부터 네 마리 소의 품질 점수를 곱한 값
multiple = []
# 원래 품질 점수
S = 0
for i in range(N):
    res = A[i]
    for j in range(i + 1, i + 4):
        res *= A[j % N]
    multiple.append(res)
    S += res

# 장난친 소의 번호 (원래 소 번호가 1부터 시작하므로 -1)
Q = list(map(lambda x: int(x) - 1, input().split()))

# 장난친 소 되돌리기
for idx in Q:
    # 장난친 소가 포함된 값 바꾸기
    for i in range(idx - 3, idx + 1):
        multiple[i % N] *= -1
        S += 2 * multiple[i % N]
    print(S)