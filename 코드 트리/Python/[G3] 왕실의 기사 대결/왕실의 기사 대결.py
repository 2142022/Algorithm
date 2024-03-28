from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 기사s가 d방향으로 이동이 가능한 지 여부와 연쇄적으로 밀리는 기사들의 번호
def is_possible(s, sd):
    # 기사 s의 범위
    sr, sc, sh, sw, _, _ = people[s]

    # 연쇄적으로 밀리는 기사들의 번호
    idxs = {s}

    # 방문 체크
    visited = [[0] * L for _ in range(L)]

    # 탐색 칸을 담은 큐
    q = deque()
    for r in range(sr, sr + sh):
        for c in range(sc, sc + sw):
            visited[r][c] = 1
            q.append((r, c, s))

    while q:
        r, c, i = q.popleft()

        # 사방 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 체크
            if not (0 <= nr < L and 0 <= nc < L):
                # 원래 밀리는 방향인 경우, 이동 불가
                if d == sd:
                    return 0, idxs
                continue

            # 벽 체크
            if board[nr][nc] == 2:
                # 원래 밀리는 방향인 경우, 이동 불가
                if d == sd:
                    return 0, idxs
                continue

            # 방문 체크
            if visited[nr][nc]:
                continue

            # 밀리는 방향 외의 다른 방향에서는 현재 기사와 같은 사람이어야만 함
            if d != sd:
                ir, ic, ih, iw, _, _ = people[i]
                if ir <= nr < ir + ih and ic <= nc < ic + iw:
                    q.append((nr, nc, i))
                    visited[nr][nc] = 1

            # 밀리는 방향에서는 기사 있으면 큐에 추가
            else:
                for key, value in people.items():
                    vr, vc, vh, vw, _, _ = value
                    if vr <= nr < vr + vh and vc <= nc < vc + vw:
                        q.append((nr, nc, key))
                        visited[nr][nc] = 1
                        idxs.add(key)
                        break

    return 1, idxs

################################################################################

# 이동 & 체력 감소
def move(a, idxs, d):
    for num in idxs:
        r, c, h, w, k, z = people[num]

        # 이동
        r += dr[d]
        c += dc[d]

        # 초기 기사는 이동만 함
        if num == a:
            people[num] = [r, c, h, w, k, z]
            continue

        # 함정 수 확인
        cnt = 0
        for i in range(r, r + h):
            for j in range(c, c + w):
                if board[i][j] == 1:
                    cnt += 1

        # 함정이 체력 이상인 경우 소멸
        if cnt >= k:
            people.pop(num)

        # 체력 감소 & 대미지 증가
        else:
            k -= cnt
            z += cnt
            people[num] = [r, c, h, w, k, z]

################################################################################

# 체스판 크기, 기사 수, 명령 수
L, N, Q = map(int, input().split())

# 체스판
board = [list(map(int, input().split())) for _ in range(L)]

# 기사 정보 (위치, 크기, 체력, 데미지)
people = defaultdict(list)
for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    people[i] = [r, c, h, w, k, 0]

# 사방 탐색용
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# 명령
for _ in range(Q):
    # 이동할 기사, 이동 방향
    i, d = map(int, input().split())

    # 이미 소멸한 기사인 경우 패스
    if i not in people:
        continue

    # 현재 기사가 이동이 가능한 지 여부와 연쇄적으로 밀리는 기사들의 번호
    possible, idxs = is_possible(i, d)

    # 이동이 가능한 경우, 이동하기
    if possible:
        move(i, idxs, d)

# 생존자의 대미지 합
res = 0
for r, c, h, w, k, z in people.values():
    res += z
print(res)