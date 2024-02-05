from collections import defaultdict
import sys
input = sys.stdin.readline

# 한 대각선(좌하 - > 우상)씩 비숍 두기
# idx: 대각선의 인덱스 (행 + 열)
# cnt: 현재까지 놓은 비숍 개수
def dfs(idx, cnt):
    global N, max_cnt

    # 모든 대각선(좌하 -> 우상)을 탐색한 경우, 최대 비숍 개수 갱신
    if idx == 2 * N - 1 or idx == 2 * N:
        max_cnt = max(max_cnt, cnt)
        return

    # 남은 대각선 모두 비숍을 뒀을 때 max_cnt 이하인 경우 탐색X
    if cnt + (2 * N - idx) // 2 <= max_cnt:
        return

    # 현재 대각선에 비숍 두기
    for i, j in possible[idx]:
        if diag[i - j] == 0:
            diag[i - j] = 1
            dfs(idx + 2, cnt + 1)
            diag[i - j] = 0

    # 현재 행에 비숍을 두지 않고 넘어가기
    dfs(idx + 2, cnt)

#################################################################################################################

# 체스판 크기
N = int(input())

# 체스판의 각 대각선(좌하 -> 우상)별로 비숍을 놓을 수 있는 (행, 열)
possible = defaultdict(list)
for i in range(N):
    for j, num in enumerate(list(map(int, input().split()))):
        if num == 1:
            possible[i + j].append((i, j))

# 이미 놓인 대각선(좌상 -> 우하) 체크
diag = defaultdict(int)

# 짝수칸에 놓을 수 있는 비숍의 최대 개수
max_cnt = 0
# 한 대각선(좌하 -> 우상)씩 비숍 두기
dfs(0, 0)
max_cnt_even = max_cnt

# 홀수칸에 놓을 수 있는 비숍의 최대 개수
max_cnt = 0
# 한 대각선(좌하 -> 우상)씩 비숍 두기
dfs(1, 0)
max_cnt_odd = max_cnt

print(max_cnt_even + max_cnt_odd)