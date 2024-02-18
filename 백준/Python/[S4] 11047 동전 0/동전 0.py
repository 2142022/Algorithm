import sys
input = sys.stdin.readline

# 동전 종류, 만들고자 하는 가치
N, K = map(int, input().split())

# 동전의 가치
A = [int(input()) for _ in range(N)]

# 필요한 동전 최소 개수
cnt = 0

# 사용할 수 있는 최대 가치의 동전 인덱스
i = N - 1
while K:
    # 현재 동전의 가치
    v = A[i]

    # 현재 동전 최대로 사용하기
    d, m = divmod(K, v)
    cnt += d
    K = m
    i -= 1

print(cnt)