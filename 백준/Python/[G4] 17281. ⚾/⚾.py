from itertools import permutations
import sys
input = sys.stdin.readline

# 이닝 수
N = int(input())

# 각 이닝에서 각 선수가 얻는 결과
# innings[i][j]: i번째 이닝에서 j번째 선수가 얻는 결과
innings = [list(map(int, input().split())) for _ in range(N)]

# 최대 점수
max_score = 0

# 선수 순서 정하기
for i in permutations(range(1, 9), 8):
    # 선수 순서 (0번 선수는 4번째 타자)
    order = list(i)
    players = order[:3] + [0] + order[3:]

    # 점수, 아웃 수
    score = out = 0

    # 1루, 2루, 3루에 사람이 있는지 없는지 체크
    b1 = b2 = b3 = 0

    # 타자 선수
    idx = 0

    # 끝날 때까지 반복
    n = 0
    while n < N:
        # 현재 타자 선수
        p = players[idx]

        # 현재 선수가 친 공
        ball = innings[n][p]

        # 안타
        if ball == 1:
            score += b3
            b3, b2, b1 = b2, b1, 1

        # 2루타:
        elif ball == 2:
            score += b2 + b3
            b3, b2, b1 = b1, 1, 0

        # 3루타:
        elif ball == 3:
            score += b1 + b2 + b3
            b3, b2, b1 = 1, 0, 0

        # 홈런
        elif ball == 4:
            score += 1 + b1 + b2 + b3
            b3 = b2 = b1 = 0

        # 아웃
        else:
            out += 1
            if out == 3:
                n += 1
                b1 = b2 = b3 = 0
                out = 0

        # 다음 선수
        idx = (idx + 1) % 9

    # 점수 비교
    max_score = max(max_score, score)

print(max_score)