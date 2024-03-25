import sys
input = sys.stdin.readline

# cnt번째 날 게임 진행
# killed: 현재까지 죽은 참가자 번호
# guilty: 참가잗들의 유죄 지수
def play(cnt, killed, guilty):
    global max_cnt

    # 마피아가 죽었거나 시민 모두 죽은 경우, 게임 끝
    if mafia in killed or len(killed) == N - 1:
        max_cnt = max(max_cnt, cnt)
        if max_cnt == N // 2:
            return 1
        return 0

    # 낮: 유죄 지수가 가장 높은 사람 죽이기
    if (N - len(killed)) % 2:
        # 죽일 사람
        i = guilty.index(max(guilty))
        killed.add(i)
        guilty[i] = -10000

    # 마피아가 죽었거나 시민 모두 죽은 경우, 게임 끝
    if mafia in killed or len(killed) == N - 1:
        max_cnt = max(max_cnt, cnt)
        if max_cnt == N // 2:
            return 1
        return 0

    # 밤: 한 명 죽이기
    for i in range(N):
        if i in killed or i == mafia:
            continue

        nkilled = {k for k in killed}
        nguilty = guilty[:]
        nkilled.add(i)
        nguilty[i] = -10000

        # 다른 참가자들의 유죄 지수 갱신
        for j in range(N):
            if j not in killed:
                nguilty[j] += R[i][j]

        # 다음 날 게임 진행
        if play(cnt + 1, nkilled, nguilty):
            return 1

    return 0

##############################################################################

# 참가자 수
N = int(input())

# 유죄 지수
guilty = list(map(int, input().split()))

# 마피아가 시민을 죽일 때, 참가자들이 얻게 되는 유죄 지수
R = [list(map(int, input().split())) for _ in range(N)]

# 마피아 번호
mafia = int(input())

# 죽은 사람 번호
killed = set()

# 최대 밤의 횟수
max_cnt = 0
play(0, killed, guilty)
print(max_cnt)