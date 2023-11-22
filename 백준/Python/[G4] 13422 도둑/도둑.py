import sys
input = sys.stdin.readline

# 테스트케이스 수
T = int(input())
for _ in range(T):
    # 집의 수, 돈을 훔칠 연속된 집의 수, 자동 방법 장치가 작동하는 최소 돈
    N, M, K = map(int, input().split())

    # 각 집이 보관중인 돈
    house = list(map(int, input().split()))
    # 원형이므로 더 늘리기
    if N != M:
        house += house[:M - 1]

    # 돈을 훔칠 수 있는 방법의 수
    cnt = 0

    # M개의 집의 돈을 훔쳤을 때의 돈
    money = 0

    # 처음 M개의 집 훔치기
    for i in range(M):
        money += house[i]
    if money < K:
        cnt += 1

    # 이후 뒤의 집 추가, 앞의 집 삭제하여 훔친 돈 구하기
    for i in range(M, len(house)):
        money += house[i] - house[i - M]
        if money < K:
            cnt += 1

    print(cnt)