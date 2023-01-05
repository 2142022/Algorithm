import sys
input = sys.stdin.readline

# 식량창고 개수
N = int(input())

# 각 식량창고의 식량 개수
food = list(map(int, input().split()))

# i번째 식량창고까지의 최대 약탈 식량 개수
cnt = [0] * N

# 0번째와 1번째 식량창고를 같이 약탈 불가능하므로 각자 초기화
cnt[0] = food[0]
cnt[1] = food[1]

for i in range(2, N):
    # (i - 1번째까지의 약탈 개수)와 (i - 2번째까지의 약탈 개수 + i번째 식량 개수) 비교
    cnt[i] = max(cnt[i - 1], cnt[i - 2] + food[i])

print(cnt[N - 1])
