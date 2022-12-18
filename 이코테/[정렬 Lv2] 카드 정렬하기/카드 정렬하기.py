import heapq
import sys
input = sys.stdin.readline

# 카드 묶음 수
N = int(input())

# 각 카드 묶음의 카드 수를 담는 최소 힙
card = []
for i in range(N):
    heapq.heappush(card, int(input()))

# 최소 카드 비교 횟수
result = 0
while len(card) != 1:
    # 가장 작은 크기의 묶음 2개 더하기
    cnt = heapq.heappop(card) + heapq.heappop(card)

    # 더한 카드를 다시 card에 넣기
    heapq.heappush(card, cnt)

    result += cnt

print(result)