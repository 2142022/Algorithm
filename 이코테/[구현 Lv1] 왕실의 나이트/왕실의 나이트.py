import sys
input = sys.stdin.readline

# 특정 위치의 나이트가 이동할 수 있는 위치 (8가지)
dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

# 나이트의 위치 입력받기 (strip()을 통해서 한 문자씩 입력받기)
c, r = map(str, input().strip())

# 나이트가 이동할 수 있는 경우의 수
cnt = 0

# 8가지 위치 이동해보기
for i in range(8):
    nr = int(r) + dr[i]
    nc = ord(c) + dc[i]     # ord: 아스키코드로 변환

    # 정원을 벗어나지 않았다면 경우의 수 + 1
    if 1 <= nr <= 8 and ord('a') <= nc <= ord('h'):
        cnt += 1

print(cnt)