from itertools import permutations
import sys
input = sys.stdin.readline

# 이닝 수
N = int(input())

# 각 선수가 각 이닝에서는 얻는 결과
players= [list(map(int, input().split())) for _ in range(N)]

# 최대 득점
max_score = 0

# 선수 순서
for perm in permutations(range(1, 9), 8):
    perm_list = list(perm)
    order = perm_list[:3] + [0] + perm_list[3:]

    # 이닝 수, 현재 타자 (번호가 아닌 9명 중의 순서), 총 점수. 아웃 수
    cnt = p = score = out = 0

    # 각 루에 선수가 있는지 체크
    e1 = e2 = e3 = 0

    # 끝날 때까지 반복
    while cnt < N:
        # 현재 타자의 번호
        player = order[p]

        # 현재 타자가 얻는 결과
        result = players[cnt][player]

        # 안타
        if result == 1:
            score += e3
            e1, e2, e3 = 1, e1, e2

        # 2루타
        elif result == 2:
            score += e2 + e3
            e1, e2, e3 = 0, 1, e1

        # 3루타
        elif result == 3:
            score += e1 + e2 + e3
            e1, e2, e3 = 0, 0, 1

        # 홈런
        elif result == 4:
            score += e1 + e2 + e3 + 1
            e1, e2, e3 = 0, 0, 0

        # 아웃
        else:
            out += 1
            if out == 3:
                cnt += 1
                out = 0
                e1, e2, e3 = 0, 0, 0

        # 다음 선수
        p = (p + 1) % 9

    # 점수 비교
    max_score = max(max_score, score)

print(max_score)