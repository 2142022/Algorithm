import sys
input = sys.stdin.readline

# i행에서 모든 경사로를 설치할 수 있는지 확인
# P: 경사로를 설치해야 하는 구간
def possible(i, P):
    # 설치한 열 체크
    visited = [0] * N

    # 설치 구간
    for start, end, h in P:
        for j in range(start, end + 1):
            # 높이가 h가 아닌 경우 설치 불가
            if board[i][j] != h:
                return False

            # 이미 경사로가 설치되어 있는 경우 설치 불가
            if visited[j]:
                return False
            visited[j] = 1

    # 모든 경사로를 설치한 경우
    return True

##########################################################################

# 지도에서 지나갈 수 있는 행의 개수 세기
def get_cnt():
    global cnt

    # 행
    for i in range(N):
        # 경사로 설치 구간
        pos = []

        # 한 칸씩 탐색
        for j in range(1, N):
            # 이전 칸의 높이, 현재 칸의 높이
            ph, nh = board[i][j - 1], board[i][j]

            # 높이가 2 이상 차이나는 경우 경사로 설치 불가
            if abs(ph - nh) > 1:
                break

            # 높이 차이가 1인 경우 경사로 설치 구간
            if ph < nh:
                if j - L < 0:
                    break
                pos.append((j - L, j - 1, ph))
            elif ph > nh:
                if j + L - 1 >= N:
                    break
                pos.append((j, j + L - 1, nh))

        # 모든 경사로를 설치할 수 있는 경우, 지나갈 수 있는 행
        else:
            if possible(i, pos):
                cnt += 1

##########################################################################

# 지도 크기, 경사로 길이
N, L = map(int, input().split())

# 지도
board = [list(map(int, input().split())) for _ in range(N)]

# 지나갈 수 있는 길의 개수
cnt = 0

# 현재 지도에서 지나갈 수 있는 행의 개수 세기
get_cnt()

# 지도 회전
board = list(map(list, zip(*board[::-1])))

# 회전한 지도에서 지나갈 수 있는 행의 개수 세기
get_cnt()

print(cnt)