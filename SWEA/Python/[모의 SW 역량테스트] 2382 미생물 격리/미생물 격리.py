from collections import defaultdict

# 미생물 이동
def move(microbe):
    # 이동 후의 미생물 수와 이동 방향
    after = defaultdict(list)

    # 한 칸씩 이동
    for k, v in microbe.items():
        # 현재 위치, 미생물 수, 이동 방향
        r, c = k
        t, d = v

        # 이동
        r += dr[d]
        c += dc[d]

        # 약품이 있는 곳인 경우
        if r in (0, N - 1) or c in (0, N - 1):
            t //= 2
            d = (d + 2) % 4

        # 이동 후 위치 담기
        if t:
            after[(r, c)].append([t, d])

    # 한 칸에 여러 군집이 있는 경우, 합치기
    res = defaultdict(list)
    for k, v in after.items():
        v.sort(key = lambda x: -x[0])
        d = v[0][1]
        t = 0
        for x, y in v:
            t += x
        res[k] = [t, d]

    return res

#########################################################################

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 구역 크기, 격리 시간, 미생물 군집 수
    N, M, K = map(int, input().split())

    # 각 위치별 미생물 수와 이동 방향
    microbe = defaultdict(list)
    for _ in range(K):
        r, c, t, d = map(int, input().split())
        d = {1: 0, 2: 2, 3: 3, 4: 1}[d]
        microbe[(r, c)] = [t, d]

    # M시간 동안 미생물 이동
    for _ in range(M):
        microbe = move(microbe)

    # 남아있는 미생물 수의 총 합
    print(f'#{TC} {sum([x[0] for x in microbe.values()])}')
