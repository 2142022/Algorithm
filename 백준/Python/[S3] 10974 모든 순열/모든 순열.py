import sys
input = sys.stdin.readline

# 숫자 하나씩 탐색
def dfs(idx):
    # 순열을 만들었다면 출력
    if idx == N:
        print(*nums)
        return

    # 다음 수 탐색
    for i in range(1, N + 1):
        if i not in nums:
            nums.append(i)
            dfs(idx + 1)
            nums.pop()

###########################################3

# 수의 개수
N = int(input())

# 순열
nums = []

# 숫자 하나씩 탐색
dfs(0)