from collections import defaultdict
import sys
input = sys.stdin.readline

# i행에 퀸 놓기
def dfs(i):
    global cnt

    # 모든 행에 퀸을 둔 경우 끝내기
    if i == N:
        cnt += 1
        return

    # 현재 행에 둘 수 있는 곳 탐색
    for j in range(N):
        if not col[j] and not diag1[i - j] and not diag2[i + j]:
            col[j] = diag1[i - j] = diag2[i + j] = 1
            dfs(i + 1)
            col[j] = diag1[i - j] = diag2[i + j] = 0

###########################################################################

# 체크판 크기
N = int(input())

# 퀸을 놓은 열, 대각선1(좌상 -> 우하), 대각선2(우상 -> 좌하) 체크
col = [0] * N
diag1 = defaultdict(int)
diag2 = defaultdict(int)

# 최종 경우의 수
cnt = 0

# 한 행에 하나씩 퀸 놓기
dfs(0)

print(cnt)