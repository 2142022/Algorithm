import sys
input = sys.stdin.readline

# N: 화폐 종류 수, M: 구하고자 하는 화폐 가치
N, M = map(int, input().split())

# N개의 화폐 가치
money = []
for i in range(N):
    money.append(int(input()))

# i원을 만들기 위한 최소한의 화폐 개수
cnt = [2147483647] * (M + 1)

for i in range(min(money), M + 1):
    # 각 화폐 종류별로 화폐 개수는 1
    if i in money:
        cnt[i] = 1

    # 현재 화폐 가치에서 화폐 종류별로 더하기
    for m in money:
        # M원 이하일 때만 적용
        if i + m < M + 1:
            # (기존 화폐 개수)와 (현재 화폐 개수 + 1) 비교
            cnt[i + m] = min(cnt[i + m], cnt[i] + 1)

# 2147483647이라면 만들 수 없는 금액이므로 -1 출력
if cnt[M] == 2147483647:
    print(-1)
else:
    print(cnt[M])
