import sys
input = sys.stdin.readline

# 목표 금액 P까지 가능한 경우 체크
def check(P):
    # 가능한 금액 체크
    dp = [0] * (P + 1)
    dp[0] = 1

    # 동전 선택
    for price, cnt in coins:
        # 가능한 금액을 거꾸로 생각하기
        # 순서대로 더하는 경우, 더한 결과에 또 동전을 더하게 됨
        # print(price, cnt)
        for i in range(P, price - 1, -1):
            # 이전에 기록된 금액에서 더하기
            if dp[i - price]:
                # 가능한 동전 금액만큼 더하기
                for j in range(i, min(P, i + price * cnt) + 1, price):
                    if j == P:
                        return 1
                    dp[j] = 1

    return 0

##############################################################

# 3개의 테스트케이스
for _ in range(3):
    # 동전 종류
    N = int(input())

    # 한 사람이 가져야 할 금액
    P = 0
    # 나눠야 할 동전
    coins = []
    for _ in range(N):
        price, cnt = map(int, input().split())
        coins.append((price, cnt))
        P += price * cnt

    # 총 금액이 홀수인 경우 나누기 불가능
    if P % 2:
        print(0)
        continue
    P //= 2

    # 반으로 나눌 수 있는지 확인
    print(check(P))