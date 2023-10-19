from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 이다솜 파: 0, 임도연 파: 1
isY = {'S': 0, 'Y': 1}

# 자리 배치 (S=0, Y=1로 입력받기)
seat = [list(map(lambda x: isY[x], input().rstrip())) for _ in range(5)]

# 소문난 칠공주를 결성할 수 있는 경우의 수
cnt = 0

# 사방 탐색용
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 사용한 경로 체크 (기본값은 0)
visited = defaultdict(int)

# 현재 인원, 임도연파의 인원, 경로(비트마스킹), 경로(리스트)를 담은 큐
q = deque()
for i in range(5):
    for j in range(5):
        q.append((1, seat[i][j], 1 << (i * 5 + j), [(i, j)]))

# 큐 탐색
while q:
    # 현재 인원, 임도연파의 인원, 경로(비트마스킹), 경로(리스트)
    total, ycnt, path_bit, path  = q.popleft()

    # 방문한 곳의 사방 탐색
    for r, c in path:
        for d in range(4):
            # 다음 위치
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위를 초과하면 패스
            if not (0 <= nr < 5 and 0 <= nc < 5):
                continue

            # 다음 위치(비트마스킹)
            pos_bit = 1 << (nr * 5 + nc)
            # 이미 방문한 곳 패스
            if path_bit & pos_bit:
                continue

            # 경로(비트마스킹) 갱신
            next_path_bit = path_bit + pos_bit
            # 사용한 경로 체크
            if visited[next_path_bit]:
                continue
            visited[next_path_bit] = 1

            # 임도연파는 3명까지 가능
            nycnt = ycnt + seat[nr][nc]
            if nycnt > 3:
                continue

            # 소문난 칠공주를 결성한 경우
            if total == 6:
                cnt += 1
                continue

            # 다음 위치 큐에 추가
            q.append((total + 1, nycnt, next_path_bit, path + [(nr, nc)]))

print(cnt)