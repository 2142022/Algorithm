import sys
input = sys.stdin.readline

# 세그먼트 트리 생성
def define(start, end, idx):
    if start == end:
        segment[idx] = 1
        return segment[idx]
    middle = (start + end) // 2
    segment[idx] = define(start, middle, 2 * idx) + define(middle + 1, end, 2 * idx + 1)
    return segment[idx]

###################################################################################################

# 제거할 사람(remove)의 세그먼트 트리에서의 인덱스 구하기
def find(start, end, idx, remove):
    if start == end:
        return start
    middle = (start + end) // 2
    if remove <= segment[2 * idx]:
        return find(start, middle, 2 * idx, remove)
    else:
        return find(middle + 1, end, 2 * idx + 1, remove - segment[2 * idx])

###################################################################################################

# 제거 (remove의 1을 0으로 바꾸기)
def update(start, end, idx, remove):
    segment[idx] -= 1
    if start == end:
        return 0
    middle = (start + end) // 2
    if remove <= middle:
        update(start, middle, 2 * idx, remove)
    else:
        update(middle + 1, end, 2 * idx + 1, remove)

###################################################################################################

# 사람 수, 제거할 사람의 순서
N, K = map(int, input().split())

# 제거되는 사람
remove = []

# 세그먼트 트리 생성
segment = [0] * (4 * (N + 1))
define(1, N, 1)

# 마지막으로 제거된 사람 번호
last = 1

# 한 명씩 제거
for i in range(N):
    # 제거할 사람의 번호
    last = (last + K - 1) % (N - i)
    if last == 0:
        last = N - i

    # 제거할 사람의 세그먼트 트리에서의 인덱스
    idx = find(1, N, 1, last)
    remove.append(str(idx))

    # 제거 (1을 0으로 바꾸기)
    update(1, N, 1, idx)

print('<' + ', '.join(remove) + '>')