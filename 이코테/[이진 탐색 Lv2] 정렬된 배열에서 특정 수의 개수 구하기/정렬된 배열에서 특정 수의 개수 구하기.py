import sys
input = sys.stdin.readline

# 이진 탐색을 이용하여 값이 x인 첫 원소 구하기
def find_start(x):
    global N
    start = 0
    end = N - 1

    # 첫 x의 인덱스
    idx = -1

    while start <= end:
        mid = (start + end) // 2

        # 중간값이 x이고 그 이전값이 x가 아닌 경우
        if (mid == 0 and nums[mid] == x) or (nums[mid] == x and nums[mid - 1] != x):
            idx = mid
            break
        # 첫 x가 중간 이전에 있는 경우
        elif x <= nums[mid]:
            end = mid - 1
        # 첫 x가 중간 후에 있는 경우
        else:
            start = mid + 1

    return idx

######################################################################################

# 이진 탐색을 이용하여 값이 x인 마지막 원소 구하기
def find_end(x):
    global N
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        # 중간값이 x이고 그 다음 값이 x가 아닌 경우
        if (mid == end and nums[mid] == x) or (nums[mid] == x and nums[mid + 1] != x):
            idx = mid
            break
        # 마지막 x가 중간 전에 있는 경우
        elif x < nums[mid]:
            end = mid - 1
        # 마지막 x가 중간 이후에 있는 경우
        else:
            start = mid + 1

    return idx

######################################################################################

# N: 수열의 원소의 개수, x: 찾는 값
N, x = map(int, input().split())

# 수열
nums = list(map(int, input().split()))

# 값이 x인 첫 원소의 인덱스
start = find_start(x)

# start가 -1인 경우 -1 출력
if start == -1:
    print(-1)
# 출력: end - start + 1
else:
    end = find_end(x)
    print(end - start + 1)