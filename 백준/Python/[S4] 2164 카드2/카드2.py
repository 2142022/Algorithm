from collections import deque
import sys
input = sys.stdin.readline

# 카드 수
N = int(input())

# 카드
cards = deque(range(1, N + 1))

# 카드가 한 장 남을 때까지 반복
while len(cards) != 1:
    # 가장 위에 있는 카드 버리기
    cards.popleft()

    # 가장 위에 있는 카드를 아래로 옮기기
    cards.append(cards.popleft())

# 마지막 카드 출력
print(cards.popleft())