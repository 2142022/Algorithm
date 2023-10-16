from collections import defaultdict
import sys
input = sys.stdin.readline

# 수 개수, 구간의 합을 나눌 수
N, M = map(int, input().split())

# N개의 수
A = list(map(int, input().split()))

# 누적합을 M으로 나눴을 때의 나머지
remainder = 0
# 구간의 합을 M으로 나눴을 때 나머지의 개수
cnt = defaultdict(int)
for i in range(N):
    remainder = (remainder + A[i]) % M
    cnt[remainder] += 1

# 합이 M의 배수가 되는 구간의 개수
# remainder가 r이라면, r과 r 사이의 구간의 합은 M의 배수
# 즉, r의 개수에서 2개를 뽑는 경우의 수만큼 더하기
# 단, r이 0인 경우, 1개만 뽑아도 구간의 합이 M의 배수이므로 0의 개수만큼 초기화
result = cnt[0]
for r in cnt:
    result += (cnt[r] * (cnt[r] - 1)) // 2

print(result)