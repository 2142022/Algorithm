# https://school.programmers.co.kr/learn/courses/30/lessons/42891

import heapq

def solution(food_times, k):
    # 모든 음식을 먹는 시간이 k 이하라면 -1 반환
    if sum(food_times) <= k:
        return -1

    # 남은 음식의 개수
    N = len(food_times)

    # 음식의 시간과 번호
    food = []
    for i in range(N):
        heapq.heappush(food, [food_times[i], i + 1])

    # 이전 음식의 시간
    prev = 0

    # 가장 적은 시간만큼 모든 음식 먹기
    while (food[0][0] - prev) * N <= k:
        # 현재 음식의 시간
        now = heapq.heappop(food)[0] - prev

        # 남은 시간
        k -= now * N

        # 남은 음식의 개수
        N -= 1

        prev += now

    # 남은 음식이 있다면 k번째 음식 구하기
    food.sort(key=lambda x: x[1])
    k %= N
    return food[k][1]