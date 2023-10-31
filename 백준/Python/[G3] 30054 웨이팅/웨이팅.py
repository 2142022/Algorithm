from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

# 손님 수
N = int(input())

# 손님의 도착 시각
# arrive[i] = j: 시각 i에 예약한 손님의 도착 시각은 j
arrive = defaultdict(int)
# 대기줄 정보(도착 순)를 담은 최소 힙
waiting = []
for _ in range(N):
    # 예약 시각, 도착 시각
    t1, t2 = map(int, input().split())

    arrive[t1] = t2
    heapq.heappush(waiting, (t2, t1))

# 최대 대기 시간
max_waiting = 0
# 입장한 손님 수
cnt = 0

# 시각
t = 1
while cnt < N:
    # 현재 시각에 예약한 사람이 아직 입장하지 않았으며, 늦지 않게 도착한 경우
    if 0 < arrive[t] <= t:
        max_waiting = max(max_waiting, t - arrive[t])
        arrive[t] = 0
        cnt += 1

    # 예약한 사람이 없거나 예약자가 도착하지 않은 경우
    else:
        # 현재 시각 이전에 도착한 손님이 있는 경우
        while waiting[0][0] <= t:
            # 입장하는 손님의 도착 시각과 예약 시각
            t2, t1 = heapq.heappop(waiting)

            # 이미 입장한 손님인 경우 패스
            if arrive[t1] == 0:
                continue

            # 대기줄에 있는 손님 입장
            else:
                max_waiting = max(max_waiting, t - t2)
                arrive[t1] = 0
                cnt += 1
                break

    t += 1

print(max_waiting)