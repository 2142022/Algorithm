# 1 ~ N 더하기
# x: 현재 더할 수
# s: 현재까지 더한 결과
def add(x, s):
    global N

    # 모두 더하면 끝내기
    if x == N + 1:
        return s

    # 다음 수 더하기
    return add(x + 1, s + x)

####################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 더할 최대 자연수
    N = int(input())

    # 1 ~ N 더하기
    print(f'#{t} {add(1, 0)}')