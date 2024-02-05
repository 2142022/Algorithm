# 재귀로 N ~ 1 출력
def print_num(x):
    if x == 0:
        return

    print(x, end = ' ')
    print_num(x - 1)

##########################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 출력할 최대 자연수
    N = int(input())

    # 재귀로 N ~ 1 출력
    print(f'#{t}', end = ' ')
    print_num(N)
    print()