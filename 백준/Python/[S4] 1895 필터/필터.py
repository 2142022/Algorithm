import heapq
import sys
input = sys.stdin.readline

# 중앙값 반환
# (r, c): 필터의 시작 위치
def get_med(r, c):
    # 필터가 있는 위치의 픽셀들
    pix = []
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            pix.append(img[i][j])

    # 오름차순 정렬
    pix.sort()

    # 중앙값 반환
    return pix[4]

#########################################

# 이미지 크기: R X C
R, C = map(int, input().split())

# 이미지 픽셀
img = [list(map(int, input().split())) for _ in range(R)]

# 중앙값과 비교할 값
T = int(input())

# T이상인 중앙값의 개수
cnt = 0
for i in range(R - 2):
    for j in range(C - 2):
        if get_med(i, j) >= T:
            cnt += 1

print(cnt)
