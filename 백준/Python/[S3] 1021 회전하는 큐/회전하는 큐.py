from collections import deque
import sys
input = sys.stdin.readline

# N: 큐의 크기, M: 뽑아내는 수의 개수
N, M = map(int, input().split())

# 큐 생성
q = deque(i for i in range(1, N + 1))

# 뽑아낼 수
nums = list(map(int, input().split()))

# 이동하는 최소 횟수
cnt = 0

# 하나씩 뽑기
for i in range(M):
    # left: 왼쪽으로 이동하는 횟수, right: 오른쪽으로 이동하는 횟수
    left = right = 0

    # 왼쪽으로 이동하기
    while q[0] != nums[i]:
        left += 1
        q.rotate(-1)

    # 오른쪽으로 이동하는 횟수 구하기
    right = len(q) - left

    # 이동 횟수 더하기
    cnt += min(left, right)

    # 현재 수 뽑기
    q.popleft()

print(cnt)