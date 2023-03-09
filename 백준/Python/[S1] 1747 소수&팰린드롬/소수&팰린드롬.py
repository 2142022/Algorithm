import math
import sys
input = sys.stdin.readline

# 팰린드롬인지 확인하는 함수
def palindrome(num):
    # num의 자릿수
    l = len(num)

    # 앞과 뒤를 한 칸씩 비교
    for i in range(l // 2):
        if num[i] != num[l - 1 - i]:
            return False

    return True

##############################################################################

# 소수인지 확인하는 함수
def prime(num):
    # num의 제곱근
    l = int(math.sqrt(num))

    # 약수가 있는지 확인
    for i in range(3, l + 1):
        if num % i == 0:
            return False

    return True

##############################################################################

# 숫자 입력받기
N = int(input())

# N이 1이나 2인 경우는 바로 2 출력하기
if N == 1 or N == 2:
    print(2)
else:
    # N이 짝수라면 +1
    if N % 2 == 0:
        N += 1

    # 소수이면서 팰린드롬인 수가 나올 때까지 반복
    while True:
        # 팰린드롬이면서 소수면 출력, 아니면 다음 수(짝수는 소수가 아니므로 +2) 확인
        if palindrome(str(N)) and prime(N):
            print(N)
            break
        else:
            N += 2