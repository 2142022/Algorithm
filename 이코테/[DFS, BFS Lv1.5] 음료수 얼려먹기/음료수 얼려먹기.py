from collections import deque
import sys
input = sys.stdin.readline


# BFS로 하나의 아이스크림을 세는 함수
# 이어진 아이스크림은 세면서 1로 바꾸기
# q: 아이스크림 위치 정보가 담긴 큐
def ice_cream(q):
    # N, M: 전역 변수
    global N, M

    # 사방 탐색을 위한 배열
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 큐의 원소가 없어질 때까지 반복
    while q:
        # 현재 위치 뽑기
        r, c = q.popleft()

        # 사방 탐색
        for i in range(4):
            # 탐색 위치
            nr = r + dr[i]
            nc = c + dc[i]

            # 탐색 범위를 넘어간다면 패스
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 이미 큐에 있거나 아이스크림이 아니라면 패스
            if frame[nr][nc] == 1:
                continue

            # 아이스크림이라면 큐에 넣고 방문 체크(1로 바꾸기)
            q.append([nr, nc])
            frame[nr][nc] = 1


##################################################################

# N: 얼음 틀의 세로 길이
# M: 얼음 틀의 가로 길이
N, M = map(int, input().split())

# 얼음 틀
frame = [list(map(int, input().strip())) for _ in range(N)]

# 아이스크림 개수
cnt = 0

# 아이스크림 위치 정보가 담긴 큐
q = deque()

# 얼음 틀을 하나씩 탐색하면서 아이스크림이 있으면 bfs로 탐색하기
for i in range(N):
    for j in range(M):
        # 아이스크림이라면 큐에 위치를 담고 방문 체크(1로 바꾸기)
        if frame[i][j] == 0:
            q.append([i, j])
            frame[i][j] = 1

            # 아이스크림 개수 증가
            cnt += 1

            # bfs로 하나의 아이스크림 탐색
            ice_cream(q)

# 아이스크림 개수 출력
print(cnt)
