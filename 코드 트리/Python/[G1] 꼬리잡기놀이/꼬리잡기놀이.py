from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 팀 정보 파악하기
# (i, j): 팀의 머리사람 위치
# num: 팀 번호
def build_team(i, j, num):
    line[num].append((i, j))
    board[i][j] = num

    # 인원 수
    cnt = 1

    # 다음 사람 순서대로 넣기
    q = deque([(i, j)])
    while q:
        r, c = q.popleft()

        # 4방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 사람이 있는 경우
            if (cnt == 1 and board[nr][nc] == -2) or (cnt >= 2 and -4 < board[nr][nc] < 0):
                line[num].append((nr, nc))
                board[nr][nc] = num
                cnt += 1
                q.append((nr, nc))
                break

    # 인원 수 저장
    people[num] = cnt

    # 이동 선 추가하기
    q = deque([line[num][-1]])
    while q:
        r, c = q.popleft()

        # 4방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            # 범위 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 이동 선이 있는 경우
            if board[nr][nc] == -4:
                line[num].append((nr, nc))
                board[nr][nc] = num
                q.append((nr, nc))
                break

############################################################################################################

# 공 던졌을 때의 점수
# start: 시작 행이나 열 번호
# d: 방향
def get_score(start, d):
    # 공의 위치
    if d == 0:
        r, c = start, 0
    elif d == 1:
        r, c = N - 1, start
    elif d == 2:
        r, c = start, N - 1
    else:
        r, c = 0, start

    # 공을 획득하는 사람이 있을 때까지 탐색
    while 0 <= r < N and 0 <= c < N:
        # 현재 자리가 팀의 이동선인 경우
        num = board[r][c]
        if num:
            # 사람이 있는 경우
            idx = line[num].index((r, c))
            cnt = people[num]
            if idx < cnt:
                # 머리 사람, 꼬리 사람 바꾸기
                line[num].reverse()
                line[num] = line[num][-cnt:] + line[num][:-cnt]
                # 점수
                return (idx + 1) ** 2

        # 다음 위치
        r += dr[d]
        c += dc[d]

    # 공을 획득하는 사람이 없는 경우
    return 0

############################################################################################################

# 격자 크기, 팀 수, 라운드 수
N, M, K = map(int, input().split())

# 격자
board = [list(map(lambda x: -int(x), input().split())) for _ in range(N)]

# 각 팀별 이동 선, 인원 수
line = defaultdict(list)
people = [0] * (M + 1)

# 각 팀별 이동 선 확인
num = 1
for i in range(N):
    for j in range(N):
        # 머리
        if board[i][j] == -1:
            build_team(i, j, num)
            num += 1

# 사방 탐색용
dr, dc = (0, -1, 0, 1), (1, 0, -1, 0)

# 총 점수
score = 0

# 게임 진행
for k in range(1, K + 1):
    # 모든 팀 한 칸씩 이동
    for num, v in list(line.items()):
        line[num] = [v[-1]] + v[:len(v) - 1]

    # 공을 던지는 시작 방향과 위치
    d, start = divmod(k, N)
    start = (start - 1) % N
    if start == N - 1:
        d -= 1
    d %= 4
    if d > 1:
        start = N - 1 - start

    # 공 던졌을 때의 점수
    score += get_score(start, d)

print(score)
