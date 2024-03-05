from collections import deque
import sys
input = sys.stdin.readline

# 최소 이동 횟수 구하기
def get_cnt():
    # 목적지까지의 최소 이동 횟수
    min_cnt = W * H

    # cnt[k][i][j]: (i, j)에 k번의 말의 움직임을 이용해서 갈 수 있는 최소 이동 횟수
    cnt = [[[W * H] * W for _ in range(H)] for _ in range(K + 1)]
    for i in range(K + 1):
        cnt[i][0][0] = 0

    # 탐색 위치, 말의 움직임 횟수, 이동 횟수를 담은 큐
    q = deque([(0, 0, 0, 0)])
    while q:
        # 현재 위치, 말의 움직임 횟수, 이동 횟수
        r, c, k, t = q.popleft()

        # 최소 이동 횟수가 아닌 경우 패스
        if t != cnt[k][r][c]:
            continue

        # 도착 지점인 경우 끝내기
        if r == H - 1 and c == W - 1:
            min_cnt = min(min_cnt, t)
            continue

        # 말의 움직임
        if k < K:
            for nr, nc in ((r - 2, c - 1), (r - 2, c + 1), (r - 1, c - 2), (r - 1, c + 2), (r + 1, c - 2), (r + 1, c + 2), (r + 2, c - 1), (r + 2, c + 1)):
                # 범위 체크
                if not (0 <= nr < H and 0 <= nc < W):
                    continue

                # 장애물이 있는 경우 패스
                if board[nr][nc]:
                    continue

                # 이전 기록보다 적은 경우 이동
                if t + 1 < cnt[k + 1][nr][nc]:
                    cnt[k + 1][nr][nc] = t + 1
                    q.append((nr, nc, k + 1, t + 1))

        # 인접한 곳으로 이동
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < H and 0 <= nc < W):
                continue

            # 장애물이 있는 경우 패스
            if board[nr][nc]:
                continue

            # 이전 기록보다 적은 경우 이동
            if t + 1 < cnt[k][nr][nc]:
                cnt[k][nr][nc] = t + 1
                q.append((nr, nc, k, t + 1))

    # 목적지까지 갈 수 없는 경우
    if min_cnt == W * H:
        return -1

    # 목적지까지의 최소 이동 횟수
    else:
        return min_cnt

############################################################################################################################################################################

# 말의 움직임으로 움직일 수 있는 횟수
K = int(input())

# 격자판 크기
W, H = map(int, input().split())

# 격자판
board = [list(map(int, input().split())) for _ in range(H)]

# 최소 이동 횟수 구하기
print(get_cnt())
