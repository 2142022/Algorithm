# x의 각 자리 숫자 더하기
def get_sum(x):
    # 한 자리 숫자인 경우 끝내기
    if 0 <= x <= 9:
        return x

    # 다음 자리 수 더하기
    return x % 10 + get_sum(x // 10)

#################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 자연수
    N = int(input())

    # 각 자리 숫자 더하기
    print(f'#{t} {get_sum(N)}')