import sys
input = sys.stdin.readline

# 격자 크기, 날짜 수
M, N = map(int, input().split())

# 0행, 0열에 있는 애벌레 개수
T = 2 * M - 1

# 0행, 0열에 있는 애벌레들이 매일 자라는 크기의 누적합
plus = [0] * T
for _ in range(N):
    # +0, +1, +2 개수
    a, b, c = map(int, input().split())

    # +1이 되는 첫 애벌레 체크
    if a < T:
        plus[a] += 1

    # +2가 되는 첫 애벌레 체크
    if a + b < T:
        plus[a + b] += 1

# 누적합
plus[0] += 1
for i in range(1, T):
    plus[i] += plus[i - 1]

# 0행, 0열을 제외한 애벌레 크기는 왼쪽, 왼쪽 위, 위쪽 비교하지 않아도 어차피 위쪽이 가장 큼
# 위쪽 애벌레 크기는 항상 동일
same = plus[T - M + 1:]

# 출력
j = T - M
for i in range(M):
    print(plus[j], *same)
    j -= 1