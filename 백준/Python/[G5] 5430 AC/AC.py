import sys
input = sys.stdin.readline

# 테스트 케이스
for _ in range(int(input())):
    # 수행할 함수
    func = input().rstrip()

    # 수의 개수
    n = int(input())

    # 배열
    x = list(map(int, input().replace(',', ' ').replace('[', ' ').replace(']', ' ').split()))

    # 앞에서 빼야 하는 숫자의 개수, 뒤에서 빼야 하는 숫자의 개수
    front = back = 0

    # 뒤집은 횟수
    rev = 0

    # 함수 실행
    for c in func:
        if c == 'R':
            rev += 1
        else:
            # 뒤집은 횟수가 짝수라면 앞에서 빼고, 홀수라면 뒤에서 빼기
            if rev % 2:
                back += 1
            else:
                front += 1

    # 삭제하는 수가 숫자 개수보다 많은 경우 error
    if front + back > n:
        print("error")

    # 함수 실행 결과 출력
    else:
        # 뒤집은 횟수가 홀수인 경우 뒤집어서 출력
        if rev % 2:
            print(f'[{",".join(map(str, reversed(x[front:n - back])))}]')
        else:
            print(f'[{",".join(map(str, x[front:n - back]))}]')
