from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 최소 힙
h = []
for _ in range(int(input())):
    # 숫자
    num = int(input())

    # 자연수라면 추가, 0이라면 삭제
    if num > 0:
        heappush(h, num)
    else:
        if h:
            print(heappop(h))
        else:
            print(0)