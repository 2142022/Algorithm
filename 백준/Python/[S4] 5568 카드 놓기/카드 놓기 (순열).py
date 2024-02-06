from itertools import permutations
import sys
input = sys.stdin.readline

# 카드 개수
n = int(input())

# 선택하는 카드의 개수
k = int(input())

# n개의 카드 입력받기
card = []
for _ in range(n):
    card.append(int(input()))

# 만들 수 있는 정수
result = set()

# k개 선택하기
for select in permutations(card, k):
    # 뽑은 숫자들로 정수 만들기
    num = 0
    for i in select:
        num = num * 10 ** len(str(i)) + i

    # set에 넣기
    result.add(num)

print(len(result))