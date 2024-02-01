from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 상근이가 페스티벌에 갈 수 있는지 확인
def bfs(n, sr, sc, er, ec):
    # 현재 위치를 담은 큐
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()

        # 현재 위치에서 1000 미터 내에 있는 편의점이나  탐색
        for nr, nc in pos.keys():
            if abs(nr - r) + abs(nc - c) <= 1000:
                # 페스티벌이라면 끝내기
                if nr == er and nc == ec:
                    return "happy"

                if not pos[(nr, nc)]:
                    pos[(nr, nc)] = 1
                    q.append((nr, nc))

    # 페스티벌에 가지 못하는 경우
    return "sad"

###############################################################

# 테스트 케이스
for _ in range(int(input())):
    # 편의점 개수
    n = int(input())

    # 상근이네 집 좌표
    sr, sc = map(int, input().split())

    # 편의점 + 페스티벌 방문체크
    pos = defaultdict(int)
    for _ in range(n):
        pos[tuple(map(int, input().split()))] = 0

    # 페스티벌 좌표
    er, ec = map(int, input().split())
    pos[(er, ec)] = 0

    # 페스티벌에 갈 수 있는지 확인
    print(bfs(n, sr, sc, er, ec))
