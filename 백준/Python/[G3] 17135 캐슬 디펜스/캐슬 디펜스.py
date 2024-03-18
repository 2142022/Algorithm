from itertools import combinations
import sys
input = sys.stdin.readline

# 적 죽이기
def kill():
    # 죽일 적의 위치
    pos = set()

    # 궁수 한 명씩 가장 가까운 적 선택
    for c in combs:
        e = sorted([(i, j) for i, j in enemy if abs(N - i) + abs(c - j) <= D], key = lambda x: (abs(N - x[0]) + abs(c - x[1]), x[1]))
        if e:
            pos.add(e[0])

    # 적 죽이기
    for i in range(len(enemy) - 1, -1, -1):
        r, c = enemy[i]
        if (r, c) in pos:
            enemy.pop(i)

    return len(pos)

###############################################################################################################################################

# 격자 크기, 궁수 공격 거리 제한
N, M, D = map(int, input().split())

# 적의 위치
enemy_origin = []
for i in range(N):
    row = list(map(int, input().split()))
    for j, info in enumerate(row):
        if info:
            enemy_origin.append([i, j])

# 제거한 적의 최대 수
max_cnt = 0

# 궁수 위치 정하기
for combs in combinations(range(M), 3):
    # 적의 위치 복사
    enemy = [e[:] for e in enemy_origin]

    # 죽인 적의 수
    cnt = 0

    # 게임 진행
    while enemy:
        # 적 죽이기
        cnt += kill()

        # 적 이동
        for i in range(len(enemy) - 1, -1, -1):
            r, c = enemy[i]

            # 성에 도착
            if r + 1 == N:
                enemy.pop(i)

            # 이동
            else:
                enemy[i][0] += 1

    # 죽인 적의 수 비교
    max_cnt = max(max_cnt, cnt)

print(max_cnt)