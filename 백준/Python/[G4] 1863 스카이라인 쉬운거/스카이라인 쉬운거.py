import sys
input = sys.stdin.readline

# 건물 고도가 바뀌는 지점 개수
n = int(input())

# 최소 건물 개수
cnt = 0

# 건물 높이를 담은 스택 (오름차순)
stack = []
for _ in range(n):
    # 건물 고도가 바뀌는 지점의 x, y 좌표
    x, y = map(int, input().split())

    # 스택의 마지막 건물보다 작은 경우, 스택에 있는 마지막 건물은 탐색 완료
    while stack and y < stack[-1]:
        stack.pop()
        cnt += 1

    # 스택의 마지막 건물과 높이가 같은 경우, 하나의 건물이므로 패스
    if stack and y == stack[-1]:
        continue

    # 0이 아닌 현재 건물 스택에 추가
    if y:
        stack.append(y)

# 스택에 남아있는 건물 개수만큼 추가
print(cnt + len(stack))