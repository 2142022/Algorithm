import sys
input = sys.stdin.readline

# 사람 수
N = int(input())

# 사람별 몸무게와 키
people = [list(map(int, input().split())) for _ in range(N)]

# 사람별 등수
rank = [1] * N
for i in range(N):
    x, y = people[i]
    for j in range(i + 1, N):
        p, q = people[j]

        # 덩치가 큰 사람 체크
        if x > p and y > q:
            rank[j] += 1
        elif x < p and y < q:
            rank[i] += 1

print(*rank)