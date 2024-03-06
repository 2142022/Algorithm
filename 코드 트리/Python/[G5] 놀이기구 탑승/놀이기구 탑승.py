from collections import defaultdict
import sys
input = sys.stdin.readline

# 총 점수 구하기
def get_score():
    # 총 점수
    score = 0

    # 모든 칸 탐색
    for r in range(n):
        for c in range(n):
            # 현재 학생 번호
            num = board[r][c]

            # 좋아하는 학생 수
            cnt = 0
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] in S[num]:
                    cnt += 1

            # 점수 갱신
            if cnt:
                score += 10 ** (cnt - 1)

    return score

################################################################################

# 학생i 탑승하기
def find_pos(i):
    # 최대 좋아하는 사람 수, 비어있는 칸 수, 그 위치
    mp, me, mr, mc = -1, -1, -1, -1

    # 모든 칸 탐색
    for r in range(n):
        for c in range(n):
            # 비어있는 경우만 탐색
            if board[r][c]:
                continue

            # 사방 탐색
            p, e = 0, 0
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < n:
                    # 비어있는 칸
                    if board[nr][nc] == 0:
                        e += 1
                    # 좋아하는 학생
                    elif board[nr][nc] in S[i]:
                        p += 1

            # 좋아하는 사람의 수가 3 이상이라면 위치 확정
            if p >= 3:
                return r, c

            # 좋아하는 사람 수 비교
            if p > mp:
                mp, me, mr, mc = p, e, r, c
            elif p == mp:
                # 비어있는 칸 수 비교
                if e > me:
                    me, mr, mc = e, r, c

    return mr, mc

################################################################################

# 격자 크기
n = int(input())

# 놀이기구
board = [[0] * n for _ in range(n)]

# 각 학생이 좋아하는 학생
S = defaultdict(list)
for _ in range(n * n):
    i, *s = map(int, input().split())
    S[i] = s

    # 탑승하기
    r, c = find_pos(i)
    board[r][c] = i

# 총 점수 구하기
print(get_score())