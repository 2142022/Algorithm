# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 문자열
    s = input().rstrip()

    # 반복되는 문자를 삭제한 문자열
    stack = []
    for c in s:
        # 전에 같은 문자가 있다면 삭제
        if stack and c == stack[-1]:
            stack.pop()
        # 전에 같은 문자가 없다면 저장
        else:
            stack.append(c)

    print(f'#{t} {len(stack)}')