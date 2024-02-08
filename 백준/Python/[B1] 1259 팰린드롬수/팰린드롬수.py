import sys
input = sys.stdin.readline

while True:
    num = input().rstrip()

    # 0이 입력되면 끝내기
    if num == '0':
        break

    # 팰린드롬 확인
    if num == num[::-1]:
        print('yes')
    else:
        print('no')