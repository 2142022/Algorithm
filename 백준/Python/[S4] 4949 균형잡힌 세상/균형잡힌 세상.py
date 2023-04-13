from collections import deque
import sys
input = sys.stdin.readline

# '.'만 입력될 때까지 입력받기
while True:
    str = input().rstrip()

    # '.'이면 끝내기
    if str == '.':
        break

    # 균형을 이루면 True, 아니면 False
    flag = True

    # 시작 괄호를 담는 큐
    start = deque()

    # 문자열의 한 문자씩 탐색
    for c in str:
        # 시작 괄호라면 큐에 담기
        if c == '(' or c == '[':
            start.append(c)

        # 닫는 괄호라면 큐에서 뽑아서 비교하기
        # 큐가 비어있거나 큐에서 뽑은 값이 짝이 아니면 끝내기
        elif c == ')' and (len(start) == 0 or start.pop() != '('):
            flag = False
            break
        elif c == ']' and (len(start) == 0 or start.pop() != '['):
            flag = False
            break

    # 큐에 시작 괄호가 남아있다면 불균형
    if len(start) != 0:
        flag = False

    # 결과 출력
    if flag:
        print('yes')
    else:
        print('no')

