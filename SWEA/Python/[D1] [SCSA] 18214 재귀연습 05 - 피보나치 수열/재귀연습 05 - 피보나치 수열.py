# 피보나치 수열 구하기
def fibo(x):
    global N

    # 1이나 2인 경우, 1 반환
    if x == 1 or x == 2:
        return 1

    # 이미 저장된 값이 있다면 반환
    if F[x] != 1:
        return F[x]

    F[x] = fibo(x - 1) + fibo(x - 2)
    return F[x]

###########################################

# 피보나치 수열
F = [1] * 31

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 구하고 싶은 피보나치 수열의 인덱스
    N = int(input())

    # 피보나치 수열 구하기
    print(f'#{t} {fibo(N)}')