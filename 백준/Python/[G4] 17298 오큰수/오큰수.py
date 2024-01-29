import sys
input = sys.stdin.readline

# 수열 A의 크기
N = int(input())

# 수열 A
A = list(map(int, input().split()))

# 아직 오큰수가 정해지지 않은 수들을 담은 스택
stack = []

# 각 수에 대한 오큰수 (오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수)
NGE = [-1] * N
for i, num in enumerate(A):
    # 현재 숫자보다 작은 수들의 오큰수는 현재 숫자
    while stack and stack[-1][1] < num:
        NGE[stack.pop()[0]] = num

    # 현재 숫자 저장
    stack.append((i, num))

print(*NGE)
