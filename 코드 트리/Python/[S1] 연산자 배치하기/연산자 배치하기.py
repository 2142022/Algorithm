import sys
input = sys.stdin.readline

# 최종 연산 구하기
# idx: 현재까지 한 연산 수
# result: 현재까지의 연산 결과
def get_res(idx, result):
    global min_res, max_res

    # 모든 연산이 끝난 경우
    if idx == n - 1:
        # 최솟값, 최댓값 비교
        min_res = min(min_res, result)
        max_res = max(max_res, result)
        return

    # 덧셈
    if cnt[0]:
        cnt[0] -= 1
        get_res(idx + 1, result + nums[idx + 1])
        cnt[0] += 1

    # 뺄셈
    if cnt[1]:
        cnt[1] -= 1
        get_res(idx + 1, result - nums[idx + 1])
        cnt[1] += 1

    # 곱셈
    if cnt[2]:
        cnt[2] -= 1
        get_res(idx + 1, result * nums[idx + 1])
        cnt[2] += 1

    return

###############################################################

# 정수 수
n = int(input())

# n개의 정수
nums = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈 개수
cnt = list(map(int, input().split()))

# 연산 결과의 최솟값과 최댓값
min_res, max_res = 1000000000, -1000000000

# 모든 연산 구하기
get_res(0, nums[0])

print(min_res, max_res)