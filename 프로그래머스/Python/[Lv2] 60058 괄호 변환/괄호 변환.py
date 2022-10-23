# https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3

# 올바른 괄호 문자열인지 체크
def is_right(p):
    # '('이면 +1, ')'이면 -1
    # 음수가 나오면 올바른 괄호 문자열이 아님
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    return True

# 현재 균형잡힌 괄호 문자열 now와 뒤의 올바른 괄호 문자열 back을 이용하여 올바른 괄호 문자열 만들기
def change(now, back):
    result = '(' + back + ')'

    # now의 앞뒤 하나씩 제외하고 괄호 반대로 추가하기
    for i in range(1, len(now) - 1):
        if now[i] == '(':
            result += ')'
        else:
            result += '('

    return result

def solution(p):
    # p를 균형잡힌 괄호 문자열로 나누기
    balance = []

    # '('가 나오면 +1, ')'가 나오면 -1
    cnt = 0

    # 균형잡힌 문자열
    string = ''
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        string += p[i]

        # cnt가 0이 되면 하나의 균형잡힌 문자열이 완성됨
        if cnt == 0:
            balance.append(string)
            string = ''

    # 올바른 괄호 문자열로 변환한 결과
    result = ''

    # 마지막 균형잡힘 괄호 문자열부터 하나씩 차례대로 올바른 괄호 문자열로 바꾸기
    for i in range(len(balance) -1, -1, -1):
        # 올바른 괄호 문자열인 경우
        if is_right(balance[i]):
            result = balance[i] + result

        # 올바른 괄호 문자열이 아닌 경우
        else:
            result = change(balance[i], result)

    return result
