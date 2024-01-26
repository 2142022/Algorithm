from collections import defaultdict
import sys
input = sys.stdin.readline

# DFS로 한 행당 퀸 하나씩 두기
# i: 현재 행
def dfs(i):
    global N, cnt

    # 모든 퀸을 둔 경우
    if i == N:
        cnt += 1
        return

    # 퀸을 둘 곳 선택
    for j in range(N):
        if not col[j] and not dg1[i - j] and not dg2[i + j]:
            col[j] = 1
            dg1[i - j] = 1
            dg2[i + j] = 1
            dfs(i + 1)
            col[j] = 0
            dg1[i - j] = 0
            dg2[i + j] = 0

################################################################

# 체스판 크기 및 퀸 개수
N = int(input())

# N개의 퀸을 둘 수 있는 경우의 수
cnt = 0

# 열별 퀸을 둔 곳 체크
col = [0] * N
# 대각선 (좌상 -> 우하) 퀸을 둔 곳 체크
dg1 = defaultdict(int)
# 대각선 (우상 -> 좌하) 퀸을 둔 곳 체크
dg2 = defaultdict(int)

# DFS로 한 행당 퀸 하나씩 두기
dfs(0)

print(cnt)