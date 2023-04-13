import sys
input = sys.stdin.readline

# 수열 A의 길이
N = int(input())

# 수열 A (원소가 중복될 수 있으므로 set으로 입력받기)
A = set(map(int, input().split()))

# 가장 큰 원소
max_num = max(A)

# 소수면 True, 아니면 False
prime = [True] * (max_num + 1)

# 에라토스테네스 체를 이용하여 소수 체크
for i in range(2, max_num + 1):
    # 이미 소수가 아닌 것으로 체크가 되어 있으면 넘어가기
    if prime[i] == False:
        continue

    # i의 배수들 모두 지우기
    j = 2
    while i * j <= max_num:
        prime[i * j] = False
        j += 1

# 최소공배수
lcm = -1

# 수열 A에서 소수인 수들 곱하기
for i in A:
    if prime[i]:
        lcm *= i

# 최소공배수가 -1이 아니라면 음수의 상태이므로 -1 곱하기
if lcm != -1:
    print(-lcm)
else:
    print(lcm)