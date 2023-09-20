import sys
input = sys.stdin.readline

# N까지의 수들 중 소수 구하기
def get_prime(N):
    # 소수 체크
    prime_flag = [1] * (N + 1)

    # 2부터 배수 삭제
    for i in range(2, N + 1):
        # 이미 삭제되었다면 패스
        if not prime_flag[i]:
            continue

        # 첫 번째는 소수, 그 뒤로 배수 삭제
        prime.append(i)
        for j in range(2 * i, N + 1, i):
            prime_flag[j] = 0

# 원하는 수
N = int(input())

# N까지의 수들 중 소수
prime = []
get_prime(N)

# 연속된 소수의 합으로 N을 만들 수 있는 경우의 수
cnt = 0

# 소수 개수
l = len(prime)

# i번째 소수부터의 합 구하기
for i in range(l):
    # i번째 소수
    s = prime[i]

    # N이라면 경우의 수 추가
    if s == N:
        cnt += 1

    # 다음 소수들 합하기
    for j in range(i + 1, l):
        s +=  + prime[j]

        # N이라면 경우의 수 추가
        if s == N:
            cnt += 1
        # N보다 크다면 패스
        elif s > N:
            break

print(cnt)