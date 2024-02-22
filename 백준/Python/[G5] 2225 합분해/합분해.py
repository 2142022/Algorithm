import sys
input = sys.stdin.readline

# i번째 숫자 더하기
# s: 현재까지의 합
def plus(i, s):
    # K개의 숫자를 더한 경우
    if i == K:
        if s == N:
            return 1
        return 0

    # 이미 전에 구해 놓을 값이 있는 경우
    if cnt[i][s]:
        return cnt[i][s]

    # 현재 수에 어떤 수를 더해도 N을 만들 수 없는 경우 끝내기
    if s + N * (K - i) < N:
        return 0

    # 현재 수 정하기
    for num in range(N + 1):
        # N을 초과하는 경우 끝내기
        if s + num > N:
            break
        cnt[i][s] = (cnt[i][s] + plus(i + 1, s + num)) % M

    return cnt[i][s]

########################################################################

# 합이 되야 하는 수, 더할 수의 개수
N, K = map(int, input().split())

# 나눌 수
M = 1000000000

# cnt[i][j]: i번째 숫자까지 더했을 때 j가 나오는 경우의 수
cnt = [[0] * (N + 1) for _ in range(K + 1)]

# 숫자 하나씩 더하기
print(plus(0, 0))