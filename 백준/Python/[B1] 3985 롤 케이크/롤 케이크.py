import sys
input = sys.stdin.readline

# 롤 케이크 길이
L = int(input())
# 각 롤 케이크를 가져간 사람의 번호
cake = [0] * (L + 1)

# 방청객 수
N = int(input())

# 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호와 그 개수
idx1, cnt1 = 0, 0
# 실제로 가장 많은 조각을 받은 방청객의 번호와 그 개수
idx2, cnt2 = 0, 0

# 방청객 탐색
for i in range(1, N + 1):
    # 원하는 케이크 시작과 끝
    P, K = map(int, input().split())

    # 가장 많은 조각을 받을 것으로 기대하고 있던 방청객과 비교
    expect = K - P + 1
    if expect > cnt1:
        idx1, cnt1 = i, expect

    # 실제로 받는 조각의 개수
    real = 0
    for j in range(P, K + 1):
        if cake[j] == 0:
            real += 1
            cake[j] = i
    if real > cnt2:
        idx2, cnt2 = i, real

print(idx1)
print(idx2)