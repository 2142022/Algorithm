from collections import defaultdict
import sys
input = sys.stdin.readline

# 물고기 이동
def fish_move():
    global fishes

    # 새로운 위치
    new = defaultdict(lambda : defaultdict(int))

    # 모든 물고기
    for k, v in fishes.items():
        # 위치
        r, c = k

        # 방향별 수
        for d, cnt in v.items():
            # 8방 탐색
            for i in range(8):
                nd = (d - i) % 8
                nr, nc = r + dr[nd], c + dc[nd]

                # 범위 체크
                if not (0 <= nr < N and 0 <= nc < N):
                    continue

                # 상어 체크
                if (nr, nc) == (sr, sc):
                    continue

                # 냄새 체크
                if (nr, nc) in smell:
                    continue

                # 이동
                new[(nr, nc)][nd] += cnt
                break

            # 이동 불가
            else:
                new[(r, c)][d] += cnt

    fishes = new

################################################################################

# cnt: 현재까지 이동한 횟수
# r, c: 현재 상어 위치
# v: 방문 위치
def shark_move(move_cnt, r, c, v):
    global visited, sr, sc, max_cnt

    # 3번 모두 이동하면 끝
    if move_cnt == 3:
        # 현재 경로로 이동했을 때 죽인 물고기 수
        cnt = 0
        for i in v:
            if i in fishes:
                cnt += sum(fishes[i].values())
        if cnt > max_cnt:
            max_cnt = cnt
            sr, sc = r, c
            visited = v
        return

    # 사방 탐색 (상좌하우)
    for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
        # 범위 체크
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        nv = {i for i in v}
        nv.add((nr, nc))
        shark_move(move_cnt + 1, nr, nc, nv)

################################################################################

# 격자 크기
N = 4

# 물고기 수, 연습 횟수
M, S = map(int, input().split())

# 각 칸의 방향별 물고기 개수
fishes = defaultdict(lambda : defaultdict(int))
for _ in range(M):
    r, c, d = map(lambda x: int(x) - 1, input().split())
    fishes[(r, c)][d] += 1

# 상어 위치
sr, sc = map(lambda x: int(x) - 1, input().split())

# 냄새의 남은 시간
smell = defaultdict(int)

# 8방 탐색용
dr, dc = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)

# 연습
for _ in range(S):
    # 현재 물고기 저장
    memo = {k: v for k, v in fishes.items()}

    # 물고기 이동
    fish_move()

    # 상어 이동 & 죽은 물고기 삭제
    visited = set()
    max_cnt = -1
    shark_move(0, sr, sc, set())
    for v in visited:
        if v in fishes:
            fishes.pop(v)
            smell[v] = 3

    # 모든 냄새의 남은 시간 -1
    for k, v in list(smell.items()):
        if v == 1:
            smell.pop(k)
        else:
            smell[k] -= 1

    # 물고기 복제 완료
    for k, v in memo.items():
        for d, cnt in v.items():
            fishes[k][d] += cnt

# 남아있는 물고기 수
cnt = 0
for v in fishes.values():
    cnt += sum(v.values())
print(cnt)