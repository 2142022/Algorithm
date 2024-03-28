from collections import  defaultdict, deque
import sys
input = sys.stdin.readline

# 레이저 공격할 최단 경로 찾기
# (sr, sc): 시작 위치
# (er, ec): 도착 위치
def get_path(sr, sc, er, ec):
    # 방문 체크
    visited = set()

    # 탐색 위치와 경로를 담을 큐
    q = deque([(sr, sc, [])])
    while q:
        r, c, path = q.popleft()

        # 도착한 경우 끝내기
        if (r, c) == (er, ec):
            return path

        # 사방 탐색
        for d in range(4):
            nr, nc = (r + dr[d]) % N, (c + dc[d]) % M

            # 이미 부서진 포탑 체크
            if (nr, nc) not in tops:
                continue

            # 방문 체크
            if (nr, nc) in visited:
                continue
            visited.add((nr, nc))

            # 경로 추가
            q.append((nr, nc, path + [(nr, nc)]))

    # 경로가 없는 경우
    return []

##################################################################################################################################

# 공격
def attack(path):
    # 레이저 공격이 불가능한 경우, 포탄 공격을 받게 되는 포탑을 경로에 담기
    if not path:
        for d in range(8):
            r, c = (er + pr[d]) % N, (ec + pc[d]) % M

            # 이미 부서진 포탑 체크
            if (r, c) not in tops:
                continue

            # 공격자 자신인지 체크
            if (r, c) == (sr, sc):
                continue

            # 공격받는 탑에 추가
            path.append((r, c))
        path.append((er, ec))

    # 공격자의 공격력
    power = tops[(sr, sc)][0]

    # 공격
    for i in range(len(path)):
        r, c = path[i]

        # 목표 탑 외의 나머지 탑
        if i < len(path) - 1:
            if tops[(r, c)][0] > power // 2:
                tops[(r, c)][0] -= power // 2
                pos.add((r, c))
            else:
                tops.pop((r, c))

        # 목표 탑
        else:
            if tops[(r, c)][0] > power:
                tops[(r, c)][0] -= power
                pos.add((r, c))
            else:
                tops.pop((r, c))

##################################################################################################################################

# 격자 크기, 라운드 수
N, M, K = map(int, input().split())

# 위치별 공격력, 공격 시점
tops = defaultdict(list)
for i in range(N):
    for j, info in enumerate(list(map(int, input().split()))):
        if info:
            tops[(i, j)] = [info, 0]

# 4방 탐색용 (우하좌상)
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
# 8방 탐색용
pr, pc = (-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)

# K 라운드 진행
for R in range(1, K + 1):
    # 공격에 관련된 탑
    pos = set()

    # 공격자, 공격할 탑
    sr, sc = sorted([(*v, *k) for k, v in tops.items()], key = lambda x: (x[0], -x[1], -(x[2] + x[3]), -x[3]))[0][2:]
    er, ec = sorted([(*v, *k) for k, v in tops.items()], key = lambda x: (-x[0], x[1], x[2] + x[3], x[3]))[0][2:]
    pos.add((sr, sc))

    # 공격자 공격력 증가, 공격 시점 갱신
    tops[(sr, sc)][0] += N + M
    tops[(sr, sc)][1] = R

    # 레이저 공격할 경로
    path = get_path(sr, sc, er, ec)

    # 공격
    attack(path)

    # 포탄이 1개 남은 경우 끝내기
    if len(tops) <= 1:
        break

    # 포탄 정비 : 공격과 관련없었던 포탑 + 1
    for top in tops.keys():
        if top not in pos:
            tops[top][0] += 1

# 가장 강한 포탑의 공격력
print(max(list(tops.values()), key = lambda x: x[0])[0])