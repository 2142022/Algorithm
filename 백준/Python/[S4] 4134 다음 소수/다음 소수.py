import sys
input = sys.stdin.readline

# 소수인지 확인하는 함수
def check_prime(x):
    # 약수가 있으면 소수X
    # 어차피 들어오는 x는 모두 홀수이므로 3부터 홀수만 확인
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

################################################

# x이상의 소수 중 가장 작은 소수 반환
def find_prime(x):
    # x가 0 ~ 2라면 2 리턴
    if 0 <= x <= 2:
        return 2

    # x가 짝수라면 어차피 소수가 아니므로 +1
    if x % 2 == 0:
        x += 1

    # x에 2씩 더해가며 소수인지 확인
    while not check_prime(x):
        x += 2

    return x

################################################

# 테스트케이스 개수
t = int(input())

# t개의 테스트케이스
for _ in range(t):
    # 가장 작은 n이상의 소수 구하기
    n = int(input())

    print(find_prime(n))
