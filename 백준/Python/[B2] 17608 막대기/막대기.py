import sys
input = sys.stdin.readline

# 막대기 개수
N = int(input())

# 보이는 막대기를 저장한 스택
stack = []
for i in range(N):
    # 현재 막대기 높이
    h = int(input())

    # 현재 막대기보다 낮은 막대기는 안 보이므로 스택에서 삭제
    while stack and stack[-1] <= h:
        stack.pop()

    # 현재 막대기 저장
    stack.append(h)

print(len(stack))