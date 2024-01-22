# DFS로 한 줄씩 색 정하기
# idx: 행 번호
# cnt: 지금까지 새로 칠한 칸 수
# c: 현재 행의 색깔
def dfs(idx, cnt, c):
    global N, M, mn

    # 모든 행을 새로 칠한 경우 끝내기
    if idx == N:
        mn = min(mn, cnt)
        return

    # 현재 행 새로 칠하기
    for i in range(3):
        if i != c:
            cnt += colors[idx][i]

    # 다음 행 탐색
    if idx < N - 2 and c == 0:
        dfs(idx + 1, cnt, c)
        dfs(idx + 1, cnt, c + 1)
    elif 1 <= idx < N - 1 and c == 1:
        dfs(idx + 1, cnt, c)
        dfs(idx + 1, cnt, c + 1)
    elif idx >= 2 and c == 2:
        dfs(idx + 1, cnt, c)

######################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 깃발 크기
    N, M = map(int, input().split())

    # i행에 있는 색의 개수 (0: W, 1: B, 2: R)
    colors = [[0] * 3 for _ in range(N)]
    for i in range(N):
        info = input().rstrip()
        # flags.append(info)
        for c in info:
            if c == 'W':
                colors[i][0] += 1
            elif c == 'B':
                colors[i][1] += 1
            else:
                colors[i][2] += 1

    # 새로 칠해야 하는 최소 칸 수
    mn = N * M

    # DFS로 한 줄씩 색 정하기
    dfs(0, 0, 0)

    print(f'#{t} {mn}')