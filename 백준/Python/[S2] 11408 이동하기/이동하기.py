import sys
input = sys.stdin.readline

# 미로 크기
N, M = map(int, input().split())

# 미로의 각 방에 있는 사탕 개수
cnt = [list(map(int, input().split())) for _ in range(N)]

# 첫 번째 행은 오른쪽으로만 이동 가능
for j in range(1, M):
    cnt[0][j] += cnt[0][j - 1]

# 두 번째 행부터는 위에서 아래로 이동하거나 왼쪽에서 오른쪽으로 이동 가능
for i in range(1, N):
    for j in range(M):
        if j == 0:
            cnt[i][j] += cnt[i - 1][j]
        else:
            cnt[i][j] += max(cnt[i - 1][j], cnt[i][j - 1])

print(cnt[N - 1][M - 1])