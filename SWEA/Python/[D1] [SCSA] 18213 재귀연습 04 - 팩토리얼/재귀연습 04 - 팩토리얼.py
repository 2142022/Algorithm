# N! 구하기
# x: 현재 곱할 수
# s: 현재까지 곱한 결과
def factorial(x, s):
    global N

    # 모두 곱하면 끝내기
    if x == N + 1:
        return s

    # 다음 수 곱하기
    return factorial(x + 1, s * x)

#########################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 곱할 최대 자연수
    N = int(input())

    # N! 구하기
    print(f'#{t} {factorial(1, 1)}')