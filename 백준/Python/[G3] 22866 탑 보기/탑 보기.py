from collections import defaultdict
import sys
input = sys.stdin.readline

# 건물 수
N = int(input())

# 건물 높이
H = [0] + list(map(int, input().split()))

# 각 건물에서 볼 수 있는 건물들 중 가장 가까운 건물 (거리가 같은 경우, 왼쪽 건물)
closest = defaultdict(int)

# 각 건물에서 볼 수 있는 건물 개수
cnt = defaultdict(int)

# 왼쪽에서 탐색했을 때, 건물 높이가 감소하도록 건물 번호를 담은 스택
stack = []
for i in range(1, N + 1):
    # 현재 건물의 높이
    h = H[i]

    # 현재 건물보다 작거나 같은 건물들 삭제
    while stack and H[stack[-1]] <= h:
        stack.pop()

    # 스택에 남은 건물들은 현재 건물보다 높으므로 볼 수 있음
    cnt[i] += len(stack)

    # 현재 건물의 왼쪽에서 볼 수 있는 가장 가까운 건물은 스택의 마지막
    if stack:
        closest[i] = stack[-1]

    # 현재 건물 스택에 추가
    stack.append(i)

# 오른쪽에서 탐색했을 때, 건물 높이가 감소하도록 건물 번호를 담은 스택
stack = []
for i in range(N, 0, -1):
    # 현재 건물의 높이
    h = H[i]

    # 현재 건물보다 작거나 같은 건물들 삭제
    while stack and H[stack[-1]] <= h:
        stack.pop()

    # 스택에 남은 건물들은 현재 건물보다 높으므로 볼 수 있음
    cnt[i] += len(stack)

    # 현재 건물의 오른쪽에서 볼 수 있는 가장 가까운 건물은 스택의 마지막
    if stack:
        idx = stack[-1]

        # 왼쪽에서 볼 수 있는 건물과의 거리 비교
        if closest[i] and i - closest[i] > idx - i:
            closest[i] = idx
        elif not closest[i]:
            closest[i] = idx

    # 현재 건물 스택에 추가
    stack.append(i)

# 각 건물에서 볼 수 있는 건물 개수와 가장 가까운 건물 출력
for i in range(1, N + 1):
    if cnt[i]:
        print(cnt[i], closest[i])
    else:
        print(0)