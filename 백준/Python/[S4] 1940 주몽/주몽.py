from itertools import combinations
import sys
input = sys.stdin.readline

# 재료의 개수
N = int(input())

# 갑옷을 만드는데 필요한 수
M = int(input())

# N개의 재료들이 가진 고유한 번호
matter = list(map(int, input().split()))

# 갑옷을 만들 수 있는 경우의 수
cnt = 0

# 두 개씩 뽑아서 M이 되면 cnt 증가
for i, j in combinations(matter, 2):
    if i + j == M:
        cnt += 1

print(cnt)