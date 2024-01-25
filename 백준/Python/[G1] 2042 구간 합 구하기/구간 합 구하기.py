import sys
input = sys.stdin.readline

# 세그먼트 트리 생성
def define(start, end, idx):
    if start == end:
        segment_tree[idx] = nums[start]
        return segment_tree[idx]
    middle = (start + end) // 2
    segment_tree[idx] = define(start, middle, 2 * idx) + define(middle + 1, end, 2 * idx + 1)
    return segment_tree[idx]

###########################################################################################################

# j번째 수를 +n 하기
def update(start, end, idx, j, n):
    if j < start or j > end:
        return
    segment_tree[idx] += n
    if start != end:
        middle = (start + end) // 2
        update(start, middle, 2 * idx, j, n)
        update(middle + 1, end, 2 * idx + 1, j, n)

###########################################################################################################

# i번째 수부터 j번째 수까지의 합 구하기
def get_prefix(start, end, idx, i, j):
    if j < start or i > end:
        return 0
    if i <= start and j >= end:
        return segment_tree[idx]
    middle = (start + end) // 2
    return get_prefix(start, middle, 2 * idx, i, j) + get_prefix(middle + 1, end, 2 * idx + 1, i, j)

###########################################################################################################

# 수의 개수, 변경 횟수, 합 구하는 횟수
N, M, K = map(int, input().split())

# N개의 수
nums = [int(input()) for _ in range(N)]

# 세그먼트 트리 생성
segment_tree = [0] * (4 * N)
define(0, N - 1, 1)

# 변경 혹은 구간합 구하기
for _ in range(M + K):
    a, b, c = map(int, input().split())

    # b번째 수를 c로 변경
    if a == 1:
        update(0, N - 1, 1, b - 1, c - nums[b - 1])
        nums[b - 1] = c

    # b번째 수부터 c번째 수까지의 합 구하기
    if a == 2:
        print(get_prefix(0, N - 1, 1, b - 1, c - 1))

