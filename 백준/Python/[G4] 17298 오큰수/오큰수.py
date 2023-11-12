import sys
input = sys.stdin.readline

# 수열 A의 크기
N = int(input())
# 수열 A
A = list(map(int, input().split()))

# 오큰수
NGE = [-1] * N

# A의 원소와 인덱스를 하나씩 담는 스택
stack = []
for i in range(N):
    # 현재 숫자
    num = A[i]

    # 현재 숫자가 스택의 마지막 원소보다 큰 경우, 스택에 있는 수의 오큰수는 현재 숫자
    while stack and num > stack[-1][0]:
        # 스택의 마지막 숫자 및 인덱스
        sn, si = stack.pop()

        # 오큰수 갱신
        NGE[si] = num

    # 현재 숫자와 인덱스를 스택에 추가
    stack.append((num, i))

print(*NGE)