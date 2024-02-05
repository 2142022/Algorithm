# 재귀로 1 ~ N 출력
def print_num(x):
    global N

    # 모든 수를 출력한 경우 끝내기
    if x == N + 1:
        return

    print(f'{x}', end=" ")
    print_num(x + 1)

###############################################

# 테스트케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 출력할 최대 자연수
    N = int(input())

    # 재귀로 1 ~ N 출력
    print(f'#{t}', end = ' ')
    print_num(1)
    print()