import sys
input = sys.stdin.readline

# 정수 하나씩 선택하기
# idx: 선택하는 수의 인덱스
def get_sum(idx):
    global N, S, cnt

    # 모든 수를 탐색한 경우
    if idx == N:
        # 부분 수열의 합이 S인 경우
        if nums and sum(nums) == S:
            cnt += 1
        return

    # 현재 수를 선택하지 않는 경우
    get_sum(idx + 1)

    # 현재 수를 선택하는 경우
    nums.append(A[idx])
    get_sum(idx + 1)
    nums.pop()

##############################################

# 정수 개수, 수열의 합
N, S = map(int, input().split())

# N개의 정수
A = list(map(int, input().split()))

# 부분 수열
nums = []

# 합이 S가 되는 부분 수열의 개수
cnt = 0

# 정수 하나씩 선택하기
get_sum(0)

print(cnt)