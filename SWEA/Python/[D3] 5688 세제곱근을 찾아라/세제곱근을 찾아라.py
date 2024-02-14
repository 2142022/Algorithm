# N의 세제곱근 찾기
def find_root():
    # 찾을 범위
    start, end = 1, N
    while start <= end:
        # 범위 내 중간값
        mid = (start + end) // 2

        # 중간값의 세제곱
        num = mid ** 3

        # 세제곱근을 찾은 경우
        if num == N:
            return mid

        # 범위 이동
        if num > N:
            end = mid - 1
        else:
            start = mid + 1

    # 세제곱근이 없는 경우
    return -1

###############################################

# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 양의 정수
    N = int(input())

    # 양의 세제곱근 찾기
    print(f'#{T} {find_root()}')