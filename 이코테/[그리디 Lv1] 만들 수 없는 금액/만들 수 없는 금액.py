import sys
input = sys.stdin.readline

# 동전의 개수
N = int(input())

# N개의 동전
coin = list(map(int, input().split()))

# 동전 오름차순 정렬
coin.sort()

# 가장 작은 금액의 동전이 1이 아니라면 무조건 만들 수 없는 금액의 최솟값은 1
if coin[0] != 1:
    print(1)
else:
    # 이전 동전들의 합
    money = coin[0]

    # 동전의 금액이 연속되지 않는다면 이전 동전들을 모두 더했을 때 현재 동전과 비교
    # 이전 동전들의 합이 (현재 동전 - 1)보다 작다면 만들 수 없는 금액은 (이전 동전들의 합 + 1)
    for i in range(1, len(coin)):
        if coin[i] != coin[i - 1] + 1 and coin[i] > money + 1:
            break

        money += coin[i]

    # 탐색한 동전들의 합 + 1
    print(money + 1)