from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

# 소수면 True, 아니면 False
prime = [True] * 1001
prime[0] = prime[1] = False

# 에라토스테네스의 체 이용
for i in range(2, 1001):
    # 소수가 아닌 경우 패스
    if not prime[i]:
        continue

    # 현재 수는 소수
    # 현재 수의 배수들은 소수가 아니므로 지우기
    j = 2
    while i * j < 1001:
        prime[i * j] = False
        j += 1

# 테스트케이스 개수
T = int(input())

# T개의 테스트케이스
for _ in range(T):
    # 정수
    K = int(input())

    # K미만의 수 중 소수인 수들
    nums = []
    for i in range(2, K):
        # 소수면 넣기
        if prime[i]:
            nums.append(i)

    # nums에서 3개의 수를 뽑아 합이 K가 된다면 끝내기
    # 가능하면 flag = True, 불가능하면 flag = False
    flag = False
    for i in combinations_with_replacement(nums, 3):
        if sum(i) == K:
            flag = True
            print(*i)
            break

    if not flag:
        print(0)