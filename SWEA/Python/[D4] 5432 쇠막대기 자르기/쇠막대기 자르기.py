# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 쇠막대기와 레이저 배치
    info = input().rstrip()

    # 잘린 쇠막대기 개수
    cnt = 0

    # 현재까지 잘린 쇠막대기를 저장하는 스택
    stack = []
    for i in range(len(info)):
        # 괄호
        c = info[i]

        # 레이저나 쇠막대기의 끝인 경우
        if c == ')':
            # 앞의 여는 괄호 꺼내기
            stack.pop()

            # 레이저인 경우 현재까지 스택에 저장된 쇠막대기 개수 더하기
            if info[i - 1] == '(':
                cnt += len(stack)

            # 쇠막대기의 끝인 경우 개수 + 1
            else:
                cnt += 1

        # 쇠막대기의 시작인 경우 저장
        else:
            stack.append(c)

    print(f'#{t} {cnt}')