from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 강의동 수, 공사구간의 수, 사용 가능한 돌의 수
N, M, K = map(int, input().split())

# 강의동에서 와두도까지 필요한 돌의 수
# 1동부터 시작하기 때문에 앞에 임의로 0 넣기
S = [0] + list(map(int, input().split()))

# 공사구간
construction = set()
for _ in range(M):
    a, b = map(int, input().split())
    construction.add((min(a, b), max(a, b)))

# 공사구간이 1개 이하라면 모든 강의장이 연결되어 있음
if M <= 1:
    print("YES")
    exit()

# 1번 강의장과 연결되어 있는 강의장들 중 와우도까지 필요한 최소 돌의 개수
first = S[1]
# 현재 강의장과 연결되어 있는 강의장들 중 와우도까지 필요한 최소 돌의 개수
cnt = 0

# 현재 강의장과 연결된 강의장들 중 가장 작은 번호
idx = 1

# 현재 강의장
for i in range(1, N + 1):
    # 현재 강의장과 연결되어 있는 강의장들 중 와우도까지 필요한 최소 돌의 개수 비교
    if idx == 1:
        first = min(first, S[i])
    else:
        cnt = min(cnt, S[i])

    # 현재 강의장이 다음 강의장과 연결되어 있지 않은 경우 (마지막 강의장 제외)
    if i != N and (i, i + 1) in construction:
        K -= cnt
        idx = i + 1
        cnt = S[idx]

    # 마지막 강의장
    elif i == N:
        # 첫 번째 강의장과 연결되어 있지 않은 경우
        if (1, N) in construction:
            K -= cnt + first
        # 첫 번째 강의장과 연결되어 있는 경우
        else:
            K -= min(cnt, first)

    # 남은 돌의 개수가 음수라면 모든 강의동 연결 불가능
    if K < 0:
        print("NO")
        exit()

# 모든 강의동 연결 가능
print("YES")

