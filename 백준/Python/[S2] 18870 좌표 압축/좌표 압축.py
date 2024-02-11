import sys
input = sys.stdin.readline

# 좌표 개수
N = int(input())

# 좌표 + 인덱스
X = list(map(lambda x:[int(x)], input().split()))
for i in range(N):
    X[i].append(i)

# 좌표 기준 오름차순 정렬
X.sort()

# 작은 좌표의 개수
cnt = [0] * N
for i in range(1, N):
    if X[i][0] == X[i - 1][0]:
        cnt[X[i][1]] = cnt[X[i - 1][1]]
    else:
        cnt[X[i][1]] = cnt[X[i - 1][1]] + 1

print(*cnt)
