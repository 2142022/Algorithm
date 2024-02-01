from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 정수 개수
N = int(input())

# 최소 힙, 최대 힙
mnh, mxh = [], []

# 정수 1개씩 추가
for _ in range(N):
    num = int(input())

    # 두 힙의 크기가 같은 경우에는 최대 힙에 넣기
    # 최대 힙이므로 부호를 반대로 넣기
    if len(mnh) == len(mxh):
        heappush(mxh, -num)
    # 최소 힙의 크기가 더 큰 경우에는 최소 힙에 넣기
    else:
        heappush(mnh, num)

    # 최소 힙의 가장 작은 수가 최대 힙의 가장 큰 수보다 작은 경우, 둘의 수 바꾸기
    # 즉, 최대 힙에는 중간값 이전의 작은 값들을, 최소 힙에는 중간값보다 큰 값들 담기
    if mnh and mxh and mnh[0] < -mxh[0]:
        mn, mx = heappop(mnh), heappop(mxh)
        heappush(mnh, -mx)
        heappush(mxh, -mn)

    # 중간값은 최대 힙의 루트
    print(-mxh[0])