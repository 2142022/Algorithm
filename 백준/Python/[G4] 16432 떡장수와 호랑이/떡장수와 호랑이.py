from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# DFS로 호랑이에게 떡을 줄 수 있는 방법 찾기
# day: 떡을 준 날의 수
# eat: 호랑이가 먹은 떡
def dfs(day, eat):
    global N, visit

    # 떡을 모두 준 경우
    if day == N:
        for i in eat:
            print(i)
        exit()

    # 현재 날짜에 먹을 수 있는 떡 체크
    for i in ricecake[day]:
        # 어제 먹은 떡은 패스
        if eat and i == eat[-1]:
            continue

        # 방문 체크
        if visit & (1 << (day * 9 + i)):
            continue
        visit |= 1 << (day * 9 + i)

        # 다음 날 탐색
        dfs(day + 1, eat[:] + [i])

######################################################

# 떡을 파는 날의 수
N = int(input())

# 날마다 먹을 수 있는 떡
ricecake = defaultdict(list)
for i in range(N):
    info = list(map(int, input().split()))
    for j in range(1, info[0] + 1):
        ricecake[i].append(info[j])

# 호랑이에게 떡을 줄 수 있는 방법
result = []

# 방문체크 (비트마스킹)
# DFS를 사용하면 완전 탐색 -> 시간 초과
# visit을 통해서 이미 탐색해본 부분은 패스
# visit[day][ricecake]를 1 << (day * 9 + ricecake)로 사용하기
visit = 0

# DFS로 방법 찾기
dfs(0, [])

print(-1)