from itertools import combinations
import sys
input = sys.stdin.readline

# 테스트 케이스
while True:
    # 뽑은 수의 개수, 뽑은 수
    k, *S = map(int, input().split())

    # 0이 입력되면 끝내기
    if k == 0:
        break

    # S에서 6개만 뽑기
    for i in combinations(S, 6):
        print(*i)
    print()