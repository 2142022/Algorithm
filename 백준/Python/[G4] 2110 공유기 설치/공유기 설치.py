import sys
input = sys.stdin.readline

# 인접한 두 공유기의 최소 거리를 dis로 했을 때 가능한지 확인
# 최대한 많은 공유기를 설치해보고 공유기의 개수가 C보다 크다면 가능
def check(dis):
    # 공유기의 개수
    cnt = 1

    # 마지막으로 설치한 공유기 위치
    last = X[0]

    for i in range(1, N):
        # 마지막 공유기와의 거리가 dis 이상이 되면 공유기 설치
        if X[i] - last >= dis:
            cnt += 1
            last = X[i]

    # 공유기의 개수가 C d이상이라면 dis 가능
    if cnt >= C:
        return True
    else:
        return False

###########################################################################
    
# N: 집의 개수, C: 공유기 개수
N, C = map(int, input().split())

# 집의 좌표 입력받은 후 정렬
X = [0] * N
for i in range(N):
    X[i] = int(input())
X.sort()

# 공유기 사이의 거리를 매개변수로 이분 탐색
left = 0
right = X[-1] - X[0]

while left <= right:
    mid = (left + right) // 2

    # 인접한 두 공유기의 거리가 최소 mid인 경우가 가능한지 확인
    # 가능하다면 mid를 더 늘리고 불가능하다면 줄이기
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)
