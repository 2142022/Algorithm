from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 수업 수
N = int(input())

# 수업의 시작 시간, 끝나는 시간 (시작 시간 기준으로 오름차순 정렬)
time = sorted([list(map(int, input().split())) for _ in range(N)])

# 각 강의실에서 할 수 있는 마지막 강의의 끝나는 시간을 저장한 최소 힙
h = []
heappush(h, 0)
for s, t in time:
    # 가장 일찍 끝나는 수업에 이어서 할 수 있는 경우
    if h[0] <= s:
        heappop(h)
        heappush(h, t)

    # 모든 강의실에서 할 수 없는 경우, 새로운 강의실 생성
    else:
        heappush(h, t)

# 강의실 개수 출력
print(len(h))