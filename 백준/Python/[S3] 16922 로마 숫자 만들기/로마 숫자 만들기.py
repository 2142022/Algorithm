from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

# 1, 5, 10, 50 중 사용할 수 있는 문자의 개수
N = int(input())

# 결과값: 4개의 원소 중 N개를 중복 조합으로 뽑아서 합의 경우의 수
# 모든 결과
result = set()

# 모든 결과를 result에 넣기
for i in combinations_with_replacement([1, 5, 10, 50], N):
    result.add(sum(i))

print(len(result))