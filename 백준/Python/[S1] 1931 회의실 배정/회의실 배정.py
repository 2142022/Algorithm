import sys
input = sys.stdin.readline

# 회의 수
N = int(input())

# 회의 시간 (시작 시간 기준으로 오름차순 정렬)
time = sorted([list(map(int, input().split())) for _ in range(N)])

# 최대한 많은 회의를 했을 때의 회의를 담은 스택
stack = []
for start, end in time:
    # 마지막 회의 다음에 할 수 있는 회의인 경우
    if not stack or (stack and start >= stack[-1][1]):
        stack.append((start, end))

    # 마지막으로 넣은 회의보다 더 빨리는 끝나는 경우, 마지막 회의 대신 현재 회의 넣기
    elif stack and end < stack[-1][1]:
        while stack and end < stack[-1][1]:
            stack.pop()
        stack.append((start, end))

print(len(stack))