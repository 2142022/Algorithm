import sys
input = sys.stdin.readline

# 스티커를 붙일 수 있는 경우 붙이기
# i, j: 노트북에서 스티커를 붙이는 시작 위치
def possible(i, j):
    for r in range(R):
        for c in range(C):
            # 스티커가 아닌 경우 패스
            if sticker[r][c] == 0:
                continue

            # 이미 노트북에 스티커가 있는 경우 끝내기
            if laptop[i + r][j + c]:
                return 0

    # 현재 스티커를 붙일 수 있는 경우
    return 1

#####################################################################################

# 현재 탐색하는 스티커 붙이기
def put():
    global cnt

    # 스티커를 붙이는 시작 위치
    for i in range(N - R + 1):
        for j in range(M - C + 1):

            # 스티커를 붙일 수 있는 경우 붙이기
            if possible(i, j):
                for r in range(R):
                    for c in range(C):
                        if sticker[r][c]:
                            laptop[i + r][j + c] = 1
                            cnt += 1
                return 1

    # 스티커를 붙일 수 없는 경우
    return 0

#####################################################################################

# 노트북 크기, 스티커 개수
N, M, K = map(int, input().split())

# 노트북에 스티커가 붙은 곳 체크
laptop = [[0] * M for _ in range(N)]

# 노트북에 스티커가 붙은 칸의 수
cnt = 0

# 스티커 탐색
for _ in range(K):
    # 스티커 크기
    R, C = map(int, input().split())

    # 스티커 모양
    sticker = [list(map(int, input().split())) for _ in range(R)]

    # 회전 횟수
    for d in range(4):
        # 90도 회전
        if d != 0:
            R, C = C, R
            sticker = list(zip(*sticker[::-1]))

        # 스티커 붙이기
        if put():
            break

# 스티커가 붙은 칸 수
print(cnt)