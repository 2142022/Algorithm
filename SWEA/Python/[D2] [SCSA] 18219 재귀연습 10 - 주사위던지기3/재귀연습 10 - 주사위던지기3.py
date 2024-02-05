# N개의 주사위 눈의 합이 M이 나오는 경우 출력
def get_perm():
    global N, M

    # 모든 주사위를 다 던진 경우 끝내기
    if len(dices) == N:
        # 주사위 눈의 합이 M인 경우에만 출력
        if sum(dices) == M:
            print(*dices)
        return

    # 현재 주사위 던지기
    for i in range(1, 7):
        dices.append(i)
        get_perm()
        dices.pop()

############################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 주사위를 던지는 횟수, 원하는 주사위 눈의 합
    N, M = map(int, input().split())

    # N개의 주사위 눈의 합이 M이 나오는 경우 출력
    print(f'#{t}')

    # 주사위 조합
    dices = []
    get_perm()
