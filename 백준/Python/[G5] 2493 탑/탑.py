import sys
input = sys.stdin.readline

# 탑의 수
N = int(input())

# 탑 높이
H = list(map(int, input().split()))

# 각 탑의 레이저 신호를 수신하는 탑의 번호
idx = [0] * N

# 각 탑의 번호와 높이를 저장한 스택
stack = []
for i in range(N, 0, -1):
    # 탐색하는 탑의 높이
    h = H[i - 1]

    # 스택에 있는 탑이 현재 탑보다 작다면 현재 탑이 신호 수신
    while stack and stack[-1][1] < h:
        idx[stack.pop()[0]] = i

    # 현재 탑 스택에 저장
    stack.append((i - 1, h))

print(*idx)