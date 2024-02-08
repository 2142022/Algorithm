from collections import Counter
import sys
input = sys.stdin.readline

# 카드 개수
N = int(input())

# 각 카드의 개수
cnt = Counter(list(map(int, input().split())))

# 구하고 싶은 카드의 개수
M = int(input())
print(*list(map(lambda x: cnt[int(x)], input().split())))