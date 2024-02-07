from collections import deque
import sys
input = sys.stdin.readline

# h 높이에서 막대를 던졌을 때 미네랄 파괴 여부, 파괴된 미네랄 위치 구하기
# cnt: 막대를 던진 차례
def shoot(h, cnt):
    # 행
    i = R - h

    # 짝수번째 막대는 왼쪽 -> 오른쪽
    if cnt % 2 == 0:
        for j in range(C):
            if M[i][j] == 1:
                M[i][j] = 0
                return 1, i, j

    # 홀수번째 막대는 오른쪽 -> 왼쪽
    else:
        for j in range(C - 1, -1 , -1):
            if M[i][j] == 1:
                M[i][j] = 0
                return 1, i, j

    # 파괴된 미네랄이 없는 경우
    return 0,

###############################################################################################

# 분리된 미네랄 클러스터링 내리기
def shift(up, down, left, right):
    # 내릴 수 있는 칸 수
    min_cnt = R

    # 미네랄 클러스터링의 각 위치 탐색
    for i in range(R):
        for j in range(C):
            if clustering[i][j]:
                # 아래의 공백 세기
                cnt = 0
                ni = i + 1
                while ni < R:
                    # 현재 클러스터링이 아닌 다른 미네랄을 만나는 경우 중지
                    if M[ni][j] and clustering[ni][j] == 0:
                        break
                    cnt += 1
                    ni += 1
                min_cnt = min(min_cnt, cnt)

    # min_cnt만큼 클러스터링 내리기
    for j in range(left, right + 1):
        for i in range(down, up - 1, -1):
            if clustering[i][j]:
                M[i + min_cnt][j] = M[i][j]
                M[i][j] = 0

###############################################################################################

# 분리된 미네랄 클러스터링이 있는지 확인
# (mr, mc): 파괴된 미네랄 위치
def check(mr, mc):
    global clustering

    # 방문 체크
    visited = [[0] * C for _ in range(R)]

    # 파괴된 미네랄의 사방 탐색
    for i, j in ((mr - 1, mc), (mr + 1, mc), (mr, mc - 1), (mr, mc + 1)):
        if not (0 <= i < R and 0 <= j < C) or visited[i][j] or not M[i][j]:
            continue

        # 현재 클러스터링
        clustering = [[0] * C for _ in range(R)]
        clustering[i][j] = 1
        visited[i][j] = 1

        # 분리된 클러스터링의 경계
        up, down, left, right = i, i, j, j

        # 탐색 위치를 담은 큐
        q = deque([(i, j)])
        while q:
            r, c = q.popleft()
            up, down, left, right = min(up, r), max(down, r), min(left, c), max(right, c)
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and M[nr][nc]:
                    visited[nr][nc] = 1
                    clustering[nr][nc] = 1
                    q.append((nr, nc))

        # 현재 클러스터링이 분리된 클러스터링인 경우
        if down != R - 1:
            shift(up, down, left, right)

###############################################################################################

# 동굴 크기
R, C = map(int, input().split())

# 미네랄
M = [list(map(lambda x: 0 if x == '.' else 1, input().rstrip())) for _ in range(R)]

# 막대를 던지는 횟수
N = int(input())

# 막대를 던지는 높이
H = list(map(int, input().split()))

# 막대 던지기
for i, h in enumerate(H):
    # 막대를 던졌을 때 미네랄 파괴 여부, 파괴된 미네랄 위치
    shoot_result = shoot(h, i)

    # 파괴된 미네랄이 없는 경우 패스
    if shoot_result[0] == 0:
        continue

    # 분리된 미네랄 클러스터링이 있는지 확인 후, 있으면 내리기
    check(shoot_result[1], shoot_result[2])

# 최종 미네랄 출력
for i in range(R):
    print(''.join(list(map(lambda x: '.' if x == 0 else 'x', M[i]))))