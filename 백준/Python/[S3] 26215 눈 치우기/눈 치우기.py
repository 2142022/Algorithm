from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

# 모든 집 앞의 눈을 치우는데 걸리는 시간 구하기
def get_time():
    # 최종 시간
    time = 0

    while h:
        # 24시간이 지난 경우 끝내기
        if time >= 1440:
            return -1

        # 두 집의 눈을 치울 수 있는 경우
        if len(h) > 1:
            n1, n2 = heappop(h), heappop(h)
            n1 += 1
            n2 += 1

            # 아직 눈이 남아있는 경우 다시 힙에 넣기
            if n1:
                heappush(h, n1)
            if n2:
                heappush(h, n2)

        # 한 집만 치우는 경우
        else:
            n = heappop(h)
            n += 1

            # 아직 눈이 남아있는 경우 다시 힙에 넣기
            if n:
                heappush(h, n)

        # 시간 증가
        time += 1

    return time

#######################################################################

# 집 수
N = int(input())

# 각 집 앞에 쌓여 있는 눈의 양을 담은 최대 힙
h = list(map(lambda x: -int(x), input().split()))
heapify(h)

# 모든 집 앞의 눈을 치우는데 걸리는 시간
print(get_time())