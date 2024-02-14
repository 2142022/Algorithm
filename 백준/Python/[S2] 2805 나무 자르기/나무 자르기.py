import sys
input = sys.stdin.readline

# h 높이로 잘랐을 때 원하는 나무 길이를 구할 수 있는지 확인
def check(mid):
    s = 0
    for i in range(N - 1, -1, -1):
        h = H[i]
        if h <= mid:
            break
        s += h - mid
        if s >= M:
            return True
    return False

############################################################

# 나무 수, 상근이가 원하는 나무의 길이
N, M = map(int, input().split())

# 나무 높이 (정렬)
H = sorted(list(map(int, input().split())))

# 설정할 높이의 범위
start, end = 0, H[-1]

# 설정할 수 있는 높이의 최댓값
max_h = 0

# 설정 높이 구하기
while start <= end:
    # 설정 높이
    mid = (start + end) // 2

    # 원하는 나무 길이를 구할 수 있는지 확인
    if check(mid):
        max_h = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_h)