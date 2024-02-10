import sys
input = sys.stdin.readline

def get_round(x):
    if (x - int(x)) >= 0.5:
        return int(x) + 1
    return int(x)

##############################################################################

# 의견 개수
n = int(input())

# 위, 아래 각각 반영하지 않을 의견의 개수
cnt = get_round(n * 0.15)

# 난이도 (정렬)
difficulty = sorted([int(input()) for _ in range(n)])[cnt:n - cnt]

if len(difficulty) == 0:
    print(0)
else:
    print(get_round(sum(difficulty) / len(difficulty)))