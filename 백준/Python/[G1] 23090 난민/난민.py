from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 난민 수
N = int(input())

# 난민의 y좌표의 중간값 이전의 y좌표를 담은 최대 힙, 중간값보다 큰 y좌표를 담은 최소 힙
mxh, mnh = [], []
# 이전 중간값, 이전 이동 거리 합
pm = pd = 0

# 난민 한 명씩 추가
for i in range(N):
    # 난민의 위치
    x, y = map(int, input().split())

    # 두 힙의 크기
    mxhl, mnhl = len(mxh), len(mnh)

    # 두 힙의 크기가 같은 경우, 최대 힙에 추가
    # 최대 힙이므로 부호를 바꿔서 저장
    if mxhl == mnhl:
        heappush(mxh, -y)
    # 최대 힙의 크기가 더 큰 경우, 최소 힙에 추가
    else:
        heappush(mnh, y)

    # 최소 힙의 루트가 최대 힙의 루트보다 작은 경우, 두 수 바꾸기
    if mnh and mxh and mnh[0] < -mxh[0]:
        mn, mx = heappop(mnh), heappop(mxh)
        heappush(mnh, -mx)
        heappush(mxh, -mn)

    # 정수시설의 위치: 난민들의 y좌표의 중간값
    mid = -mxh[0]

    # (난민의 이동 거리 합) = (이전 이동 거리 합) + (최소 힙과 최대 힙의 크기가 다른 경우, 나머지 한 명의 이동 거리) + (새로 추가된 난민의 이동 거리)
    dist = pd + (mxhl - mnhl) * abs(mid - pm) + abs(mid - y) + abs(x)

    print(mid, dist)
    pm = mid
    pd = dist
