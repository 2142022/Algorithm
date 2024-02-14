import sys
input = sys.stdin.readline

# A에 x가 있는지 확인
def is_exist(x):
    # A 내에서 찾는 범위
    start, end = 0, N - 1
    while start <= end:
        # 범위 내의 중간값
        mid = (start + end) // 2
        num = A[mid]

        # 찾는 숫자가 있다면 끝내기
        if num == x:
            return 1

        # 찾는 숫자와 중간값을 비교하여 범위 이동
        if num > x:
            end = mid - 1
        else:
            start = mid + 1

    # 끝까지 못 찾은 경우
    return 0

######################################################

# 수 개수
N = int(input())

# 정수
A = sorted(list(map(int, input().split())))

# 찾을 수의 개수
M = int(input())

# 찾을 수
X = list(map(int, input().split()))
for x in X:
    print(is_exist(x))