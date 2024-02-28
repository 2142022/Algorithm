import sys
input = sys.stdin.readline

# idx번째 외주를 할지 말지 선택
# value: 현재까지의 수익
def select(idx, value):
    global max_value

    # 모든 외주를 고른 경우
    if idx >= n:
        max_value = max(max_value, value)
        return

    # 현재 외주를 선택하는 경우
    if idx + works[idx][0] <= n:
        select(idx + works[idx][0], value + works[idx][1])

    # 현재 외주를 선택하지 않는 경우
    select(idx + 1, value)

##########################################################3

# 휴가 기간
n = int(input())

# 외주 작업 기한, 수익
works = [list(map(int, input().split())) for _ in range(n)]

# 가능한 최대 수익
max_value = 0

# 외주 하나씩 선택
select(0, 0)

print(max_value)