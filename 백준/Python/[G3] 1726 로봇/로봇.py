from collections import deque
import sys
input = sys.stdin.readline

# 도착 지점에 원하는 방향으로 이동시키는데 필요한 최소 명령 횟수 구하기
def get_cnt():
    # 사방 탐색용
    dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

    # 각 위치, 방향에 도착하는데 걸리는 최소 명령 횟수
    cnt = [[[4 * N * M] * M for _ in range(N)] for _ in range(4)]
    cnt[sd][sr][sc] = 0

    # 탐색 위치, 방향, 현재까지의 명령 횟수를 담은 큐
    q = deque([(sr, sc, sd, 0)])
    while q:
        # 현재 위치, 방향, 현재까지의 명령 횟수
        r, c, d, t = q.popleft()

        # 최소 명령 횟수가 아닌 경우 끝내기
        if t != cnt[d][r][c]:
            continue

        # 도착 지점인 경우 회전
        if (r, c) == (er, ec):
            # 회전 횟수
            plus = 0 if d == ed else 2 if (ed - d) % 4 == 2 else 1
            cnt[ed][er][ec] = min(cnt[ed][er][ec], t + plus)
            continue

        # 현재 위치에서 아무리 이동해도 최소 명령 횟수가 될 수 없는 경우 끝내기
        if t + abs(r - er) + abs(c - ec) >= cnt[ed][er][ec]:
            continue

        # 직진 (최대 3번까지 이동 가능)
        for i in range(1, 4):
            nr, nc = r + i * dr[d], c + i * dc[d]
            if not (0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0):
                break
            if t + 1 < cnt[d][nr][nc]:
                cnt[d][nr][nc] = t + 1
                q.append((nr, nc, d, t + 1))
                nr += dr[d]
                nc += dc[d]

        # 회전
        for nd, nt in (((d - 1) % 4, t + 1), ((d + 1) % 4, t + 1), ((d + 2) % 4, t + 2)):
            if nt < cnt[nd][r][c]:
                cnt[nd][r][c] = nt
                q.append((r, c, nd, nt))

    return cnt[ed][er][ec]

################################################################################################

# 공장 크기
N, M = map(int, input().split())

# 공장
board = [list(map(int, input().split())) for _ in range(N)]

# 출발 지점, 방향
sr, sc, sd = map(lambda x: int(x) - 1, input().split())
sd = {0: 1, 1: 3, 2: 2, 3: 0}[sd]

# 도착 지점, 방향
er, ec, ed = map(lambda x: int(x) - 1, input().split())
ed = {0: 1, 1: 3, 2: 2, 3: 0}[ed]

# 도착 지점에 원하는 방향으로 이동시키는데 필요한 최소 명령 횟수
print(get_cnt())