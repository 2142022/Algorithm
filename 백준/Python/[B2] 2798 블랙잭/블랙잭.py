import sys
input = sys.stdin.readline

# 카드 개수, 합 기준
N, M = map(int, input().split())

# 카드 숫자
cards = list(map(int, input().split()))

# 카드 오름차순 정렬
cards.sort()

# M과 가장 가까운 합
result = 0

# 첫 번째 카드
for i in range(N - 2):
    # 세 카드의 합
    c1 = cards[i]

    # 두 번째 카드, 세 번째 카드
    j, k = i + 1, N - 1

    while j < k:
        # 세 카드의 합
        s = c1 + cards[j] + cards[k]

        # 세 카드의 합이 M보다 작은 경우
        if s < M:
            if s > result:
                result = s
            j += 1

        # 세 카드의 합이 M인 경우 끝내기
        elif s == M:
            print(s)
            exit()

        # 세 카드의 합이 M보다 큰 경우
        else:
            k -= 1

print(result)