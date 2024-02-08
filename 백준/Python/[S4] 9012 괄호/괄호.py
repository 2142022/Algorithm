import sys
input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    stack = []
    for i in data:
        if i == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)

    if len(stack):
        print('NO')
    else:
        print('YES')