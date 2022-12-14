import heapq
import sys
input = sys.stdin.readline

# N: 시험관의 크기, K: 바이러스의 종류 개수
N, K = map(int, input().split())

# N X N 크기의 시험관
info = [list(map(int, input().split())) for _ in range(N)]

# S초 후에 (X, Y)에 존재하는 바이러스의 종류를 구하기 위한 변수
S, X, Y = map(int, input().split())

# 방문 체크(방문한 시간 저장)
visit = [[0] * N for _ in range(N)]

# 사방 탐색을 위한 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# S초 동안 반복
for s in range(S):
    # 마지막으로 증식한 바이러스의 종류와 위치 정보가 담긴 최소 힙
    virus = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] == s and info[i][j] != 0:
                heapq.heappush(virus, (info[i][j], i, j))

    # virus 증식시키기
    # virus에 원소가 없어질 때까지 반복
    while virus:
        # 바이러스 꺼내기
        # v: 바이러스 종류, (r, c): 바이러스의 위치
        v, r, c = heapq.heappop(virus)

        # 사방 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 시험관의 범위를 벗어난다면 패스
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            # 이미 바이러스가 있다면 패스
            if info[nr][nc] != 0:
                continue

            # 바이러스 증식시키고 방문 체크
            info[nr][nc] = v
            visit[nr][nc] = s + 1

# (X, Y)에 존재하는 바이러스의 종류 출력
print(info[X - 1][Y - 1])