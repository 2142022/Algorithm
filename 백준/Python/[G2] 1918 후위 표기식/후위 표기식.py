import sys
input = sys.stdin.readline

# 중위 표기식
infix = input().rstrip()
# 후위 표기식
postfix = ''

# 연산자 및 괄호 저장을 위한 스택
stack = []
for c in infix:
    # 피연산자가 나온 경우, 결과에 추가
    if 'A' <= c <= 'Z':
        postfix += c

    # '('가 나온 경우, 스택에 저장
    elif c == '(':
        stack.append(c)

    # 곱셈과 나눗셈의 경우, 앞에 있는 곱셈과 나눗셈을 결과에 추가하고 현재 연산자를 스택에 저장
    elif c == '*' or c == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            postfix += stack.pop()
        stack.append(c)

    # 덧셈과 뺄셈의 경우, 앞에 있는 모든 연산을 결과에 추가하고 현재 연산자를 스택에 저장
    elif c == '+' or c == '-':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.append(c)

    # ')'가 나온 경우, '('가 나올 때까지의 모든 연산을 결과에 추가
    elif c == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()

# 스택에 남아있는 연산자 결과에 추가
while stack:
    postfix += stack.pop()

print(postfix)