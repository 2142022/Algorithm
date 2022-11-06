import sys
input = sys.stdin.readline

# N: 볼링공의 개수, M: 볼링공의 최대 무게
N, M = map(int, input().split())

# N개의 볼링공의 무게
w = list(map(int, input().split()))

# 볼링공 오름차순 정렬
w.sort()

cnt = 0

# 현재 볼링공의 무게보다 큰 볼링공들의 개수 더하기
for i in range(N):
    for j in range(i + 1, N):
        if w[j] > w[i]:
            cnt += 1

print(cnt)