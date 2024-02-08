import sys
input = sys.stdin.readline

# 문자열 길이
L = int(input())

# 문자열 (정수로 입력받기)
nums = list(map(lambda x: ord(x) - ord('a') + 1, input().rstrip()))

# 해시값
H = 0
for i, n in enumerate(nums):
    H = (H + n * 31 ** i) % 1234567891

print(H)