import copy
from itertools import combinations
import sys
input = sys.stdin.readline

# 궁수가 공격할 수 있는 적의 수 반환
def attack():
    global D, M

    # 궁수 0, 1, 2가 공격할 적과의 거리
    md0 = md1 = md2 = D
    # 궁수 0, 1, 2가 공격할 적
    e0 = e1 = e2 = -1
    # 궁수 0, 1, 2가 공격할 적의 열
    c0 = c1 = c2 = M

    # 궁수 0, 1, 2가 공격할 적 찾기
    for i in range(len(enemy)):
        # 적의 위치
        r, c = enemy[i]

        # 궁수 0, 1, 2와의 거리
        d0 = abs(archer[0][0] - r) + abs(archer[0][1] - c)
        d1 = abs(archer[1][0] - r) + abs(archer[1][1] - c)
        d2 = abs(archer[2][0] - r) + abs(archer[2][1] - c)

        # 기존 md0, md1, md2보다 작다면 갱신
        # 거리가 같은 경우 더 왼쪽에 있다면 갱신
        if d0 < md0 or (d0 == md0 and c < c0):
            md0 = d0
            e0 = i
            c0 = c
        if d1 < md1 or (d1 == md1 and c < c1):
            md1 = d1
            e1 = i
            c1 = c
        if d2 < md2 or (d2 == md2 and c < c2):
            md2 = d2
            e2 = i
            c2 = c

    # 공격할 수 있는 적
    kill_set = {e0, e1, e2} - {-1}
    kill = list(kill_set)
    kill.sort(reverse=True)

    # 적 공격하기
    if kill:
        for i in kill:
            enemy.pop(i)
        return len(kill)
    else:
        return 0

#################################################################

# 적 이동시키기
def shift():
    global N

    for i in range(len(enemy) - 1, -1, -1):
        # 아래로 한 칸 이동
        enemy[i][0] += 1

        # 성에 도착하면 없애기
        if enemy[i][0] == N:
            enemy.pop(i)

#################################################################

# N: 격자판의 행 수, M: 격자판의 열 수, D: 궁수가 공격 가능한 거리
N, M, D = map(int, input().split())

# 적의 위치 및 적의 수
origin_enemy = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j]:
            origin_enemy.append([i, j])

# 공격할 수 있는 적의 최대 수
max_cnt = 0

# 궁수 3명 배치
for a, b, c in combinations([i for i in range(M)], 3):
    # 궁수의 위치
    archer = [(N, a), (N, b), (N, c)]

    # 적의 위치
    enemy = copy.deepcopy(origin_enemy)

    # 공격할 수 있는 적의 수
    cnt = 0

    # 게임이 끝날 때까지 반복
    while enemy:
        # 궁수가 공격할 수 있는 적의 수
        cnt += attack()

        # 적 이동
        shift()

    # 공격할 수 있는 적의 최대 수 비교
    max_cnt = max(max_cnt, cnt)

    # 모든 적을 공격할 수 있으면 끝내기
    if max_cnt == len(origin_enemy):
        break

# 공격할 수 있는 적의 최대 수 출력
print(max_cnt)
