import sys
input = sys.stdin.readline

# 교실의 크기 N X N
N = int(input())

# 자리
seat = [[0] * N for _ in range(N)]

# 사방 탐색용
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 좋아하는 학생
friends = dict()

# 자리 배치
for _ in range(N ** 2):
    # 학생A가 좋아하는 학생B, C, D, E
    A, B, C, D, E = map(int, input().split())
    friends[A] = (B, C, D, E)

    # 학생A가 앉을 자리 위치 (m, n)
    m = n = -1
    # 인접한 칸에 있는 좋아하는 학생의 수의 최대값
    max_like = 0
    # 인접한 칸에 비어있는 칸의 수의 최대값
    max_empty = 0

    # 현재 위치 (r, c)
    for r in range(N):
        for c in range(N):
            # 이미 방문한 칸은 패스
            if seat[r][c]:
                continue

            # 인접한 칸에 있는 좋아하는 학생의 수
            like = 0
            # 인접한 칸에 비어있는 칸의 수
            empty = 0

            # 사방 탐색
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 범위를 넘어가면 패스
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue

                # 좋아하는 학생이 있는 경우
                if seat[nr][nc] in (B, C, D, E):
                    like += 1
                # 비어있는 경우
                elif seat[nr][nc] == 0:
                    empty += 1

            # 좋아하는 학생의 수가 기존보다 많거나
            # 좋아하는 학생의 수는 같으면서 비어있는 칸의 수가 기존보다 많은 경우 갱신
            if like > max_like or (like == max_like and empty > max_empty):
                m = r
                n = c
                max_like = like
                max_empty = empty
            # 좋아하는 학생의 수, 비어있는 칸의 수가 0이면서 아직 자리 배정이 안 된 경우
            elif max_like == 0 and max_empty == 0 and m == -1 and n == -1:
                m = r
                n = c

    # 자리 확정
    seat[m][n] = A

# 만족도
pleasure = 0

# 만족도 조사
for r in range(N):
    for c in range(N):
        # 좋아하는 학생의 수
        cnt = 0

        # 사방 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위를 넘어가면 패스
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            # 좋아하는 학생이 있는 경우
            if seat[nr][nc] in friends[seat[r][c]]:
                cnt += 1

        if cnt:
            pleasure += 10 ** (cnt - 1)

print(pleasure)