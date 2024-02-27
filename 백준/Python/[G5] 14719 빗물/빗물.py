import sys
input = sys.stdin.readline

# 세계 크기
H, W = map(int, input().split())

# 블록 높이
blocks = list(map(int, input().split()))

# 빗물 총량
rain = 0

# 행별로 고인 빗물의 양 구하기
for i in range(H):
    # 처음으로 블록이 있는 위치
    left = 0
    for j in range(W):
        if blocks[j] >= H - i:
            left = j
            break

    # 다음으로 블록이 있는 위치 찾기
    right = left + 1
    while right < W:
        # 블록이 있는 경우 지금까지 고인 빗물 더하기
        if blocks[right] >= H - i:
            rain += right - left - 1
            left = right
        right += 1

print(rain)
