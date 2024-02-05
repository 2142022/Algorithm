# N개의 주사위 조합 출력하기
def get_comb():
    global N

    # 모든 주사위를 다 던진 경우 끝내기
    if len(dices) == N:
        print(*dices)
        return

    # 현재 주사위 던지기
    for i in range(1, 7):
        # 이전 주사위의 숫자보다 작은 경우에는 패스
        if dices and i < dices[-1]:
            continue

        dices.append(i)
        get_comb()
        dices.pop()

################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 주사위를 던지는 횟수
    N = int(input())

    # N개의 주사위 조합 출력하기
    print(f'#{t}')

    # 주사위 조합
    dices = []
    get_comb()