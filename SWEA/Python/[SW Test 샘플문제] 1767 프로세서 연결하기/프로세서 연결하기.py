import sys
sys.stdin = open("input.txt", "r")

# Core 하나씩 전원 연결하기
# idx: Core 번호
# connect: 현재까지 연결한 Core 개수
# l: 현재까지 연결한 전선의 길이
# used: core나 전선이 있는 곳 체크
def dfs(idx, connect, l, used):
    global N, cnt, length

    # 모든 Core 탐색한 경우 끝내기
    if idx == len(cores):
        if connect > cnt:
            cnt, length = connect, l
        elif connect == cnt and l < length:
            length = l
        return

    # 남은 core를 모두 더해도 현재 최대 core 개수보다 적은 경우 끝내기
    if connect + len(cores) - idx < cnt:
        return

    # Core의 위치
    r, c = cores[idx]

    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 현재 Core를 전원 연결하지 않고 패스
    dfs(idx + 1, connect, l, used)

    # 사방으로 전선 두기
    for d in range(4):
        # 현재 방향으로 전선을 뒀을 때 전원 연결이 가능한지 확인
        nr, nc, nu, nl = r + dr[d], c + dc[d], used, l
        while 0 <= nr < N and 0 <= nc < N and not nu & 1 << (N * nr + nc):
            nu |= 1 << (N * nr + nc)
            nl += 1
            nr += dr[d]
            nc += dc[d]
        if not (0 <= nr < N and 0 <= nc < N):
            dfs(idx + 1, connect + 1, nl, nu)


#####################################################################################

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 멕시노스 크기
    N = int(input())

    # 전원이 연결된 core의 최대 개수
    cnt = 0
    # 전원이 연결되지 않은 core의 위치
    cores = []
    # core나 전선이 있는 곳 체크
    used = 0
    for i in range(N):
        info = list(map(int, input().split()))
        for j in range(N):
            if info[j] == 1:
                if i == 0 or j == 0:
                    cnt += 1
                else:
                    cores.append((i, j))
                used |= 1 << (N * i + j)

    # core를 최대로 연결했을 때, 전선의 최소 길이
    length = N * N

    # DFS로 하나씩 연결해보기
    dfs(0, cnt, 0, used)

    print(f'#{t} {length}')