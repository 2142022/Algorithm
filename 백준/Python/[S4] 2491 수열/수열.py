import sys
input = sys.stdin.readline

# 숫자의 개수
N = int(input())

# N개의 숫자
nums = list(map(int, input().split()))

# cnt[0][i]: i번째 수까지 연속으로 증가한 횟수
# cnt[1][i]: i번째 수까지 연속으로 감소한 횟수
cnt = [[1] * N for _ in range(2)]

# 하나씩 탐색
for i in range(1, N):
    # 증가하면 cnt[0]를 +1, 감소하면 cnt[1]을 +1, 동일하면 모두 +1
    if nums[i] > nums[i - 1]:
        cnt[0][i] = cnt[0][i - 1] + 1
    elif nums[i] == nums[i - 1]:
        cnt[0][i] = cnt[0][i - 1] + 1
        cnt[1][i] = cnt[1][i - 1] + 1
    else:
        cnt[1][i] = cnt[1][i - 1] + 1

# cnt에서 최댓값 출력
print(max(max(cnt[0]), max(cnt[1])))