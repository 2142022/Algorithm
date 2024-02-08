from collections import Counter
import sys
input = sys.stdin.readline

# 수의 개수
N = int(input())

# N개의 수
nums = sorted([int(input()) for _ in range(N)])

# 산술평균
print(round(sum(nums) / N))

# 중앙값
print(nums[N // 2])

# 최빈값
cnt = Counter(nums).most_common()
if len(cnt) == 1 or (len(cnt) > 1 and cnt[0][1] != cnt[1][1]):
    print(cnt[0][0])
else:
    print(cnt[1][0])

# 범위
print(nums[-1] - nums[0])