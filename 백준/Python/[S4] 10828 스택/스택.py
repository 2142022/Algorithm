import sys
input = sys.stdin.readline

# 명령의 수
N = int(input())

# 스택
stack = []

# 명령
for _ in range(N):
    op, *num = input().split()

    if op == 'push':
        stack.append(num[0])
    elif op == 'pop':
        print(stack.pop() if stack else -1)
    elif op == 'size':
        print(len(stack))
    elif op == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)
