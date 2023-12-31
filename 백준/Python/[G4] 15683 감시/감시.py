import sys
input = sys.stdin.readline

# 사각 지대 탐색
# idx: CCTV 인덱스
# direction: 탐색 방향
# visited: 방문 체크
# cnt: 사각 지대 개수
def find(idx, direction, visited, cnt):
    global N, M

    # CCTV 위치
    cctv_r, cctv_c = cctv[idx][0], cctv[idx][1]

    # 사방 탐색
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 한 방향씩 탐색
    for d in direction:
        # 탐색 위치
        r, c = cctv_r + dr[d], cctv_c + dc[d]

        # 현재 방향으로 탐색
        while 0 <= r < N and 0 <= c < M:
            # 벽이 있는 경우 끝내기
            if room[r][c] == 6:
                break

            # 아직 방문하지 않은 곳만 체크
            if not (1 <= room[r][c] < 6) and not visited & 1 << (M * r + c):
                visited |= 1 << (M * r + c)
                cnt -= 1

            # 다음 위치
            r += dr[d]
            c += dc[d]

    # 다음 CCTV 탐색
    dfs(idx + 1, visited, cnt)

#############################################################################

# CCTV 하나씩 탐색
# idx: CCTV 인덱스
# visited: 방문 체크
# cnt: 사각 지대 개수
def dfs(idx, visited, cnt):
    # 모든 CCTV를 탐색한 경우 끝내기
    if idx == len(cctv):
        global blind_spot
        blind_spot = min(blind_spot, cnt)
        return

    # CCTV 번호
    num = cctv[idx][2]

    # 사각 지대 탐색
    if num == 1:
        find(idx, [0], visited, cnt)
        find(idx, [1], visited, cnt)
        find(idx, [2], visited, cnt)
        find(idx, [3], visited, cnt)

    elif num == 2:
        find(idx, [0, 1], visited, cnt)
        find(idx, [2, 3], visited, cnt)

    elif num == 3:
        find(idx, [0, 3], visited, cnt)
        find(idx, [3, 1], visited, cnt)
        find(idx, [1, 2], visited, cnt)
        find(idx, [2, 0], visited, cnt)

    elif num == 4:
        find(idx, [0, 3, 1], visited, cnt)
        find(idx, [3, 1, 2], visited, cnt)
        find(idx, [1, 2, 0], visited, cnt)
        find(idx, [2, 0, 3], visited, cnt)

    elif num == 5:
        find(idx, [0, 1, 2, 3], visited, cnt)

#############################################################################

# 사무실의 세로, 가로 크기
N, M = map(int, input().split())

# 사무실
room = []
# CCTV 위치 및 번호
cctv = []
# 사각 지대의 최소 크기
blind_spot = N * M
for i in range(N):
    info = list(map(int, input().split()))
    room.append(info)
    for j in range(M):
        k = info[j]
        if k:
            blind_spot -= 1
            if k < 6:
                cctv.append((i, j, k))

# CCTV 하나씩 탐색
dfs(0, 0, blind_spot)

print(blind_spot)