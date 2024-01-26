import sys
input = sys.stdin.readline

# 현재 수식에 대한 결과값 계산
def solve():
    global N

    # 연산을 저장하는 스택
    stack = []
    i = 0
    while i < N:
        # 괄호가 있는 경우 먼저 계산하기
        if include[i]:
            num = str(eval(expression[i:i+3]))
            i += 3

            # 스택에 있는 연산과 계산
            if stack:
                op = stack.pop()
                num1 = stack.pop()
                stack.append(str(eval(num1 + op + num)))

        # 괄호가 없는 경우
        else:
            # 현재 값
            c = expression[i]
            i += 1

            # 숫자면서 스택에 값이 있는 경우
            if '0' <= c <= '9' and stack:
                op = stack.pop()
                num = stack.pop()
                stack.append(str(eval(num + op + c)))

            # 그 외에 값 넣기
            else:
                stack.append(c)

    return int(stack[0])

#################################################################

# 괄호에 있을 연산자 선택
def dfs(idx):
    global N, result

    # 모든 연산자를 확인한 경우
    if idx == N:
        result = max(result, solve())
        return

    # 현재 연산자를 괄호에 넣지 않기
    dfs(idx + 2)

    # 현재 연산자를 괄호에 넣을 수 있는 경우 넣기
    if idx - 2 >= 0 and include[idx - 2] == 0:
        include[idx - 1:idx + 2] = [1] * 3
        dfs(idx + 2)
        include[idx - 1:idx + 2] = [0] * 3

#################################################################

# 수식의 길이
N = int(input())

# 수식
expression = input().rstrip()

# N이 1인 경우
if N == 1:
    print(expression)
    exit()

# 괄호에 있는 연산자 및 피연산자 체크
include = [0] * N

# 최대 결과값
result = solve()

# 괄호에 있을 연산자 선택
dfs(1)

print(result)