from collections import defaultdict
import sys
input = sys.stdin.readline

# 모든 파이어볼 이동
def shift(F):
    # 8방 탐색용
    dr, dc = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)

    # 새로운 파이어볼 위치
    NF = defaultdict(list)
    for k, fires in list(F.items()):
        # 위치
        r, c = k

        # 현재 칸에 있는 파이어볼 탐색
        for m, s, d in fires:
            # 이동
            nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
            NF[(nr, nc)].append([m, s, d])

    return NF

##########################################################################

# 파이어볼이 2개 이상 있는 칸은 파이어볼 나누기
def divide():
    # 파이어볼이 2개 있는 칸
    for k, fires in list(fire.items()):
        # 파이어볼 개수
        cnt = len(fires)
        if cnt >= 2:
            # 현재 칸에 있는 파이어볼들의 질량 합, 속력 합, 방향의 짝홀 합
            m_sum, s_sum, d_sum = 0, 0, 0
            for m, s, d in fires:
                m_sum += m
                s_sum += s
                d_sum += d % 2

            # 4개의 파이어볼의 질량
            m = m_sum // 5
            # 질량이 0인 경우 소멸
            if m == 0:
                fire.pop(k)
                continue

            # 4개의 파이어볼의 속력
            s = s_sum // cnt

            # 4개의 파이어볼 방향
            d = 1
            if d_sum == 0 or d_sum == cnt:
                d = 0

            # 4개의 파이어볼 저장
            fire[k] = []
            for i in range(4):
                fire[k].append([m, s, 2 * i + d])

##########################################################################

# 남아있는 파이어볼 질량 합 구하기
def get_sum():
    # 남아있는 파이어볼 질량 합
    m_sum = 0
    for k, v in fire.items():
        # 현재 위치에 있는 파이어볼
        for m, s, d in v:
            m_sum += m

    return m_sum

##########################################################################

# 격자 크기, 파이어볼 개수, 명령 수
N, M, K = map(int, input().split())

# fire[(i, j)] : (i, j)에 있는 파이어볼들의 질량, 속력, 방향
fire = defaultdict(list)
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire[(r - 1, c - 1)].append([m, s, d])

# 명령 수만큼 이동
for _ in range(K):
    # 모든 파이어볼 이동
    fire = shift(fire)

    # 파이어볼이 2개 이상 있는 칸은 파이어볼 나누기
    divide()

# 남아있는 파이어볼 질량 합 구하기
print(get_sum())
