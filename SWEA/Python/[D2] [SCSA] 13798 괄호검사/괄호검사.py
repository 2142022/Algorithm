# 닫는 괄호에 대한 짝
pair = {'}': '{', ')': '('}

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 주어지는 문자열
    s = input().rstrip()

    # 주어진 문자열에서 괄호만 저장한 스택
    stack = []
    for c in s:
        # 여는 괄호 저장
        if c == '{' or c == '(':
            stack.append(c)

        # 닫는 괄호
        elif c == '}' or c == ')':
            # 이전 괄호와 짝이라면 이전 괄호 꺼내기
            if stack and stack[-1] == pair[c]:
                stack.pop()
            # 괄호에 대한 짝이 없다면 저장
            else:
                stack.append(c)

    # 스택에 괄호가 저장되어 있다면 온전한 형태 X
    if stack:
        print(f'#{t} 0')
    else:
        print(f'#{t} 1')