from collections import deque
import sys
input = sys.stdin.readline

# 열 수 있는 문 열기
def open_door():
    # 새로 획득한 열쇠가 없을 때까지 반복
    while True:
        # 새로 획득한 열쇠 수
        cnt = 0

        # 방문 체크
        visited = [[0] * w for _ in range(h)]

        # 탐색 위치를 담은 큐
        q = deque()
        for i, j in start:
            # 출발 위치에 문이 있는데 열 수 없는 경우 패스
            if -26 <= board[i][j] < 0:
                if -board[i][j] not in key:
                    continue
                board[i][j] = 0

            # 출발 위치에 열쇠가 있는 경우
            if 0 < board[i][j] < 26:
                key.add(board[i][j])
                board[i][j] = 0
                cnt += 1

            visited[i][j] = 1
            q.append((i, j))

        while q:
            # 현재 위치
            r, c = q.popleft()

            # 사방 탐색
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if not (0 <= nr < h and 0 <= nc < w) or visited[nr][nc] or board[nr][nc] == -100:
                    continue
                info = board[nr][nc]

                # 문인 경우, 열 수 있는지 확인
                if -26 <= info < 0:
                    if -info not in key:
                        continue
                    board[nr][nc] = 0

                # 열쇠인 경우, 가지고 있는지 확인
                elif 1 <= info <= 26:
                    if info not in key:
                        key.add(info)
                        cnt += 1
                    board[nr][nc] = 0

                # 다음 위치 큐에 넣기
                visited[nr][nc] = 1
                q.append((nr, nc))

        # 새로 획득한 열쇠가 없는 경우, 더 이상 열 수 있는 문이 없으므로 끝내기
        if cnt == 0:
            break

####################################################################################################################################################################################################

# 훔칠 수 있는 문서 개수 구하기
def get_cnt():
    # 훔진 문서 개수
    cnt = 0

    # 방문 체크
    visited = [[0] * w for _ in range(h)]

    # 탐색 위치를 담은 큐
    q = deque()
    for i, j in start:
        if board[i][j] >= 0:
            # 출발 지점에 문서가 있는 경우
            if board[i][j] == 100:
                cnt += 1
                board[i][j] = 0
            visited[i][j] = 1
            q.append((i, j))

    while q:
        # 현재 위치
        r, c = q.popleft()

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if not (0 <= nr < h and 0 <= nc < w) or visited[nr][nc] or board[nr][nc] < 0:
                continue

            # 문서가 있는 경우
            if board[nr][nc] == 100:
                board[nr][nc] = 0
                cnt += 1

            # 다음 위치 큐에 넣기
            visited[nr][nc] = 1
            q.append((nr, nc))

    return cnt

####################################################################################################################################################################################################

# 테스트 케이스
for _ in range(int(input())):
    # 지도 크기
    h, w = map(int, input().split())

    # 지도 (빈 공간: 0, 벽: -100, 문서: 100, 문: -1 ~ -26, 열쇠: 1 ~ 26)
    board = []

    # 출발 위치
    start = []

    # 지도 정보 입력받기
    for i in range(h):
        # 지도 저장
        row = list(map(lambda x: -(ord(x) - ord('A') + 1) if 'A' <= x <= 'Z' else ord(x) - ord('a') + 1 if 'a' <= x <= 'z' else {'.': 0, '*': -100, '$': 100}[x], input().rstrip()))
        board.append(row)

        # 출발 위치 저장
        if i == 0 or i == h - 1:
            for j, num in enumerate(row):
                if num != -100:
                    start.append((i, j))
        else:
            if row[0] != -100:
                start.append((i, 0))
            if row[w - 1] != -100:
                start.append((i, w - 1))

    # 가지고 있는 열쇠 (1 ~ 26)
    key = set(map(lambda x: ord(x) - ord('a') + 1 if 'a' <= x <= 'z' else 0, input().rstrip()))
    if 0 in key:
        key.remove(0)

    # 열 수 있는 문 모두 열기
    open_door()

    # 훔칠 수 있는 문서 개수 구하기
    print(get_cnt())