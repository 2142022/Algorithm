import sys
input = sys.stdin.readline

# N: 1로 만들 수, K: N을 나눌 수
N, K = map(int, input().split())

# 연산 수
cnt = 0

# 1이 될 때까지 반복
while N != 1:
    # N이 K의 배수일 때, K로 나누기
    if N % K == 0:
        N //= K

    # N이 K의 배수가 아닐 때, 1씩 빼기
    else:
        N -= 1

    # 연산 횟수 1 증가
    cnt += 1

print(cnt)