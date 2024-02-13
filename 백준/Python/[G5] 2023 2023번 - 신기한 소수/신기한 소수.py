import sys
input = sys.stdin.readline

# x가 소수인지 판별 (x는 무조건 홀수)
def is_prime(x):
    # i의 배수인지 확인 (3, 5는 미리 걸렀음)
    for i in range(7, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

##################################################################

# idx 자리에 숫자 추가하기
# num: 현재 숫자
# s: 모든 자릿수의 합
def dfs(idx, num, s):
    # 원하는 자릿수가 된 경우 끝내기
    if idx == N:
        prime.append(num)
        return

    for add in (1, 3, 7, 9):
        # 모든 자릿수의 합이 3의 배수이면 그 숫자는 3의 배수
        if (s + add) % 3 == 0:
            continue

        # 소수이면 다음 수 구하기
        next = num * 10 + add
        if is_prime(next):
            dfs(idx + 1, next, s + add)

##################################################################

# 자릿수
N = int(input())

# 신기한 소수
prime = []

# 맨 앞자리부터 하나씩 숫자 추가하기
for num in (2, 3, 5, 7):
    dfs(1, num, num)

print(*prime, sep = '\n')