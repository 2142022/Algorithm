import sys
input = sys.stdin.readline

# 탑의 수
N = int(input())

# 탑의 높이
tops = list(map(int, input().split()))

# 각 탑에서 발사한 레이저 신호를 수신한 탑들의 번호
idx = [0] * N

# 레이저 신호를 수신한 탑이 없는 탑들의 번호와 높이를 담은 스택
stack = []
for i in range(N - 1, - 1, -1):
    # 레이저 신호를 보내는 탑의 높이
    h = tops[i]

    # 현재 탑이 수신할 수 있는 레이저 신호 수신하기
    # 탑의 번호가 1부터 시작하므로 +1
    while stack and h >= stack[-1][1]:
        idx[stack.pop()[0]] = i + 1

    # 현재 탑 스택에 저장
    stack.append((i, h))

print(*idx)