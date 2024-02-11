from collections import deque
import sys
input = sys.stdin.readline

# 배달해야 하는 설탕
N = int(input())

# 각 kg별 필요한 최소 봉지 개수
cnt = [-1] * 5001
cnt[3] = cnt[5] = 1

# 탐색할 설탕 무게
q = deque([3, 5])
while q:
    # 설탕 무게
    kg = q.popleft()

    # 현재 무게에 필요한 최소 봉지 개수
    c = cnt[kg]

    # 3kg 봉지
    if kg + 3 <= N and cnt[kg + 3] == -1:
        cnt[kg + 3] = c + 1
        q.append(kg + 3)

    # 5kg 봉지
    if kg + 5 <= N and cnt[kg + 5] == -1:
        cnt[kg + 5] = c + 1
        q.append(kg + 5)

print(cnt[N])