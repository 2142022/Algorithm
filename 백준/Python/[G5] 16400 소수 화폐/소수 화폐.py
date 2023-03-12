import sys
input = sys.stdin.readline

# N이하의 소수 반환 (에라토스테네스의 체)
def get_prime(N):
    # 소수인지 아닌지 확인하는 리스트
    flag = [True for _ in range(N + 1)]

    # 소수만 담은 리스트
    prime = []

    # 2부터 자신을 제외한 배수들은 False로 바꾸기
    for i in range(2, N + 1):
        if flag[i]:
            prime.append(i)

            for j in range(2 * i, N + 1, i):
                flag[j] = False

    return prime

########################################################

# 물건의 값
N = int(input())

# N이하의 소수
prime = get_prime(N)

# i원을 지불할 수 있는 경우의 수
dp = [0] * (N + 1)
dp[0] = 1

# 소수만 탐색
for p in prime:
    # 현재 화폐(p원)을 이용하여 만드는 경우의 수 추가
    for num in range(p, N + 1):
        dp[num] = (dp[num] + dp[num - p]) % 123456789

print(dp[N])