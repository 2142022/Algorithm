import sys
input = sys.stdin.readline

# 재귀로 금민수 찾기
def dfs(x):
    global A, B, cnt
    # B보다 크면 그만두기
    if x > B:
        return
    # A이상 B이하이면 cnt 증가
    elif A <= x <= B:
        cnt += 1

    dfs(x * 10 + 4)
    dfs(x * 10 + 7)

########################################

# 수의 기준
A, B = map(int, input().split())

# 금민수의 개수
cnt = 0

dfs(0)

print(cnt)