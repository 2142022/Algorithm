from collections import deque
import sys
input = sys.stdin.readline

# 사과를 먹을 수 있는 지 체크
def eat():
    # 탐색 위치, 이동 횟수, 먹은 사과 개수, 방문 체크를 담은 큐
    q = deque([(sr, sc, 0, board[sr][sc], 1 << (5 * sr + sc))])
    while q:
        # 탐색 위치, 이동 횟수, 먹은 사과 개수, 방문 체크
        r, c, shift, cnt, visited = q.popleft()

        # 3번 이동한 경우 패스
        if shift == 3:
            continue

        # 사방 탐색
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited & 1 << (5 * nr + nc):
                # 사과 체크
                ncnt = cnt
                if board[nr][nc] == 1:
                    ncnt += 1

                    # 사과를 2개 먹은 경우 끝내기
                    if ncnt == 2:
                        return 1

                # 장애물이 아닌 경우 큐에 담기
                if board[nr][nc] != -1:
                    q.append((nr, nc, shift + 1, ncnt, visited | 1 << (5 * nr + nc)))

    # 사과를 2개 이상 먹을 수 없는 경우
    return 0

##########################################################################################

# 보드
board = [list(map(int, input().split())) for _ in range(5)]

# 현재 위치
sr, sc = map(int, input().split())

# 사과를 먹을 수 있는 지 체크
print(eat())