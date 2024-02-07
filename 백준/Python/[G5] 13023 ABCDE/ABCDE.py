from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 사람 한 명씩 체크
# cnt: 고른 사람 수
# prev: 마지막으로 고른 사람
def dfs(cnt, prev):
    global flag

    # 원하는 친구 관계가 있는 경우 끝내기
    if cnt == 5:
        flag = 1
    if flag:
        return

    # 첫 번째 사람인 경우
    if cnt == 0:
        for i in range(N):
            visited[i] = 1
            dfs(cnt + 1, i)
            visited[i] = 0

    # 두 번째 사람부터는 이전 사람과 친구 관계일 때만 가능
    else:
        for i in friends[prev]:
            if not visited[i]:
                visited[i] = 1
                dfs(cnt + 1, i)
                visited[i] = 0

###########################################################

# 사람 수, 친구 관계 수
N, M = map(int, input().split())

# 친구 관계
friends = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

# 원하는 친구 관계의 여부
flag = 0

# 방문 체크
visited = [0] * N

# 사람 한 명씩 체크
dfs(0, -1)

print(flag)