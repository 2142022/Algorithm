import sys
input = sys.stdin.readline

# 문자열 길이
n = int(input())
# 문자열
origin = input().rstrip()

# 가장 긴 올바른 괄호 문자열의 길이
length = 0

# 스택에 괄호의 인덱스 넣기
stack = []
for i in range(n):
    # 현재 괄호
    now = origin[i]

    # 여는 괄호는 스택에 추가
    if now == '(':
        stack.append(i)

    # 닫는 괄호인 경우
    else:
        # 앞에 여는 괄호가 있는 경우, 올바른 괄호 문자열
        if stack and origin[stack[-1]] == '(':
            # 짝이 되는 여는 괄호 삭제
            stack.pop()

            # 가장 긴 문자열의 길이 = (현재 인덱스) - (스택의 마지막 원소)
            # 스택의 마지막 원소는 올바른 괄호 문자열을 형성하지 못한 괄호의 인덱스
            if stack:
                length = max(length, i - stack[-1])
            else:
                length = max(length, i + 1)

        # 앞에 여는 괄호가 없는 경우, 스택에 넣기
        else:
            stack.append(i)

print(length)
