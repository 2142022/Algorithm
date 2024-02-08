import sys
input = sys.stdin.readline

# 장부
stack = []
for _ in range(int(input())):
    # 부른 수
    num = int(input())

    # 0인 경우 가장 최근에 쓴 수 지우기
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))