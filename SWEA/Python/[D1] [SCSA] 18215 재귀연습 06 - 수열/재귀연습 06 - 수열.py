# 재귀로 수열 구하기
def get_num(x):
    # 첫 번째 수는 1
    if x == 1:
        return 1

    # 이전에 구한 값이라면 바로 리턴
    if nums[x] != 1:
        return nums[x]

    nums[x] = get_num(x // 2) + get_num(x - 1)
    return nums[x]

###################################################

# 수열
nums = [1] * 31

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 수열에서 구할 수의 인덱스
    N = int(input())

    # 재귀로 수열 구하기
    print(f'#{t} {get_num(N)}')
