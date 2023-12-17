from collections import deque
import sys
input = sys.stdin.readline

# 가장 자리에 있는 치즈 개수
def melt():
    # 치즈가 없는 곳
    q = deque([(0, 0)])

    # 방문 체크
    visited = 1

    # 치즈의 가장 자리
    edge = deque()
    while q:
        # 현재 위치
        r, c = q.popleft()

        # 사방 탐색
        for d in range(4):
            # 다음 위치
            nr, nc = r + dr[d], c + dc[d]

            # 범위를 벗어난 곳은 패스
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 방문 체크
            if visited & 1 << (M * nr + nc):
               continue
            visited |= 1 << (M * nr + nc)

            # 공기인 경우, 탐색 위치에 추가
            if board[nr][nc] == 0:
                q.append((nr, nc))
            # 치즈인 경우, 녹일 위치에 추가
            else:
                edge.append((nr, nc))

    # 가장 자리에 있는 치즈 녹이기
    for i, j in edge:
        board[i][j] = 0

    # 현재 녹는 치즈 개수 반환
    return len(edge)



#######################################################

# 판의 세로, 가로
N, M = map(int, input().split())
# 판
board = []
# 전체 치즈 개수
total = 0
for _ in range(N):
    row = list(map(int,  input().split()))
    board.append(row)
    total += sum(row)

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 치즈가 모두 녹는데 걸리는 시간
time = 1
while True:
    # 이번 턴에 녹는 치즈 개수
    cnt = melt()
    total -= cnt

    # 모든 치즈가 다 녹은 경우
    if total == 0:
        print(time)
        print(cnt)
        break

    time += 1
