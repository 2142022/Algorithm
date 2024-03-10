from collections import defaultdict
import sys
input = sys.stdin.readline

# 미세먼지 확산
def spread():
    # 각 칸에 더해질 미세먼지 양
    plus = defaultdict(int)

    # 모든 칸 탐색
    for r in range(R):
        for c in range(C):
            # 현재 칸의 미세먼지 양
            total = A[r][c]
            if total > 0:
                # 사방으로 확산될 미세먼지 양
                vol = total // 5
                if vol:
                    # 사방 탐색
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]

                        # 범위 체크
                        if not (0 <= nr < R and 0 <= nc < C):
                            continue

                        # 공기 청정기 위치 패스
                        if nc == 0 and nr in (up, down):
                            continue

                        # 확산
                        plus[C * nr + nc] += vol
                        A[r][c] -= vol

    # 각 칸에 미세먼지 추가
    for k, v in plus.items():
        r, c = divmod(k, C)
        A[r][c] += v

############################################################################

# 공기 청정기 작동
# start: 시작 위치
# d: 순환 방향
# t: 시계 방향인지, 반시계 방향인지 체크
def clean(start, d, t):
    # 이동시킬 미세먼지의 위치
    r, c = start, 0

    # 공기 청정기 위치가 될 때까지 반복
    while True:
        # 공기 청정기 위치인 경우 끝내기
        if A[r][c] == -1:
            nr, nc = r + dr[d], c + dc[d]
            A[nr][nc] = 0
            break

        # 현재 위치의 미세먼지 양을 다음 칸에 저장
        nr, nc = r + dr[d], c + dc[d]
        if A[nr][nc] != -1:
            A[nr][nc] = A[r][c]

        # 순환 방향 회전
        if r in (0, up, down, R - 1) and c in (0, C - 1):
            d = (d + t) % 4

        # 현재 칸에 저장시켜야 하는 미세먼지의 위치 (이전 위치)
        r -= dr[d]
        c -= dc[d]

############################################################################

# 남아있는 미세먼지의 양 구하기
def get_remain():
    # 공기 청정기 위치는 -1이므로 +2
    res = 2
    for i in range(R):
        res += sum(A[i])
    return res

############################################################################

# 방 크기, T초가 지난 후 미세먼지 양
R, C, T = map(int, input().split())

# 각 칸의 미세먼지 양
A = []

# 공기 청정기 위치 (항상 첫 번째 열에 있으므로, 행만 저장)
up, down = -1, -1
for i in range(R):
    row = list(map(int, input().split()))
    A.append(row)
    if up == -1:
        if row[0] == -1:
            up, down = i, i + 1

# 사방 탐색용 (상, 우, 하, 좌)
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

# T초 동안 반복
for _ in range(T):
    # 미세먼지 확산
    spread()

    # 공기 청정기 작동 (윗 부분, 아랫 부분 나눠서 진행)
    clean(up - 1, 2, 1)
    clean(down + 1, 0, -1)

# 남아있는 미세먼지의 양
print(get_remain())