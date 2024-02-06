import sys
input = sys.stdin.readline

# idx번재 카드 선택하기
# num: 현재까지 만들어진 정수
def dfs(idx, num):
    # k개의 카드를 뽑은 경우
    if idx == k:
        nums.add(num)
        return

    # 현재 카드 뽑기
    for i in range(n):
        if not selected[i]:
            selected[i] = 1
            dfs(idx + 1, num + cards[i])
            selected[i] = 0

###############################################

# 총 카드 수
n = int(input())

# 뽑을 카드 수
k = int(input())

# 카드
cards = [input().rstrip() for _ in range(n)]

# 선택한 카드 체크
selected = [0] * n

# 최종적으로 만들 수 있는 수 저장
nums = set()

# 카드 하나씩 뽑기
dfs(0, '')

print(len(nums))