from collections import deque
import sys
input = sys.stdin.readline

# BFS로 나이트이 최소 이동 횟수 구하기
def bfs(l, sr, sc, er, ec):
    # 팔방 탐색용
    dr, dc = (-1, -2, -2, -1, 1, 2, 2, 1), (-2, -1, 1, 2, 2, 1, -1, -2)

    # 시작 위치부터의 이동 횟수
    cnt = [[-1] * l for _ in range(l)]
    cnt[sr][sc] = 0

    # 탐색 위치를 담은 큐
    q = deque([(sr, sc)])
    while q:
        # 현재 위치, 현재 위치까지의 거리
        r, c = q.popleft()
        dist = cnt[r][c]

        # 사방 탐색
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]

            # 도착한 경우 끝내기
            if nr == er and nc == ec:
                return dist + 1

            if 0 <= nr < l and 0 <= nc < l and cnt[nr][nc] == -1:
                cnt[nr][nc] = dist + 1
                q.append((nr, nc))

#########################################################################

# 테스트 케이스
for _ in range(int(input())):
    # 체스판 크기
    l = int(input())

    # 나이트의 시작 위치
    sr, sc = map(int, input().split())

    # 나이트 도착 위치
    er, ec = map(int, input().split())

    # 두 위치가 같은 경우 이동 횟수는 0
    if sr == er and sc == ec:
        print(0)

    # BFS로 나이트의 최소 이동 횟수 출력
    else:
        print(bfs(l, sr, sc, er, ec))