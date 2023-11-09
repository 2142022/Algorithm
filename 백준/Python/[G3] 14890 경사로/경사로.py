import sys
input = sys.stdin.readline

# 현재 길을 지나갈 수 있는지 확인
def check(road):
    global N, L

    # 경사로를 놓은 위치 체크 (비트마스킹)
    exist = 0

    # 한 칸씩 탐색
    i = 1
    while i < N:
        # 현재 칸, 이전 칸 높이
        nh, ph = road[i], road[i - 1]

        # 이전 칸과 높이가 같은 경우 패스
        if nh == ph:
            i += 1

        # 이전 칸보다 높이가 작은 경우
        elif nh < ph:
            # 높이가 1차이가 아니라면 경사로 설치 불가
            if ph - nh != 1:
                return False

            # L만큼 경사로 설치
            d = 0
            while d < L:
                # 범위를 벗어난 경우 경사로 설치 불가
                if i + d >= N:
                    return False

                # 이전 칸과 높이가 같지 않은 경우 경사로 설치 불가
                if d != 0 and nh != road[i + d]:
                    return False

                exist |= 1 << (i + d)
                d += 1
            i += d

        # 이전 칸보다 높이가 큰 경우
        else:
            # 높이가 1차이가 아니라면 경사로 설치 불가
            if nh - ph != 1:
                return False

            # 이전 칸에 L만큼 경사로 설치
            d = -1
            while d >= -L:
                # 범위를 벗어낫거나 이미 경사로가 설치되어 있는 경우, 경사로 설치 불가
                if i + d < 0 or exist & 1 << (i + d):
                    return False

                # 다음 칸과 높이가 같지 않는 경우 경사로 설치 불가
                if d != -1 and ph != road[i + d]:
                    return False

                d -= 1
            i += 1

    return True

###########################################################################################

# 길의 길이, 경사로 길이
global N, L
N, L = map(int, input().split())

# 지나갈 수 있는 길의 개수
cnt = 0

# 세로 길
cols = [list() for _ in range(N)]

# 가로 길 탐색
for _ in range(N):
    # 현재 가로 길
    road = list(map(int, input().split()))

    # 각 칸을 세로 길에 추가
    for i in range(N):
        cols[i].append(road[i])

    # 현재 가로 길을 지나갈 수 있는지 확인
    if check(road):
        cnt += 1

# 세로 길 탐색
for road in cols:
    if check(road):
        cnt += 1

print(cnt)