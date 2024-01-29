import sys
input = sys.stdin.readline

# 수열 크기
n = int(input())

# 원하는 수열
nums = [int(input()) for _ in range(n)]

# 수열을 만들기 위해 필요한 연산
op = []

# 수열보다 먼저 나온 숫자를 저장한 스택
stack = []
# 현재 저장해야 할 수열의 인덱스
idx = 0
for num in range(1, n + 1):
    # 현재 숫자 저장
    stack.append(num)
    op.append('+')

    # 현재 숫자가 수열에서 원하는 숫자인 경우
    while stack and stack[-1] == nums[idx]:
        stack.pop()
        idx += 1
        op.append('-')

# 수열을 모두 탐색하지 못한 경우
if idx != n:
    print("NO")
else:
    for i in op:
        print(i)
