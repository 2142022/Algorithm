import sys
input = sys.stdin.readline

# 숫자
nums = list(map(lambda x: int(x) % 10, input().split()))

# 검증수
result = 0
for i in nums:
    result += i * i
print(result % 10)