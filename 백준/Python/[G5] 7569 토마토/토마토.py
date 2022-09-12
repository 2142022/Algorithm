from collections import deque
import sys
input = sys.stdin.readline

# 토마토가 모두 익었는지 체크하는 함수
def check():
    global M, N, H
    flag = 1

    for h in range(H):
        for n in range(N):
            for m in range(M):

                # 하나라도 안 익은 토마토가 있으면 0 반환
                if tomato[h][n][m] == 0:
                    flag = 0
                    return 0
    return 1

# 토마토가 모두 익을 때까지 최소 며칠이 걸리는지 구하는 함수
def solve():
    global M, N, H

    # 며칠 째인지
    date = 0

    # 익은 토마토의 위치를 큐에 넣기
    queue = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 1:
                    queue.append([h, n, m, date])

    # 앞, 뒤, 좌, 우, 상, 하 비교
    dh = [0, 0, 0, 0, -1, 1]
    dn = [-1, 1, 0, 0, 0, 0]
    dm = [0, 0, -1, 1, 0, 0]

    # queue의 원소가 없을 때까지 탐색
    while queue:
        # 탐색할 토마토의 위치와 현재 며칠 째인지 구하기
        tmp_h, tmp_n, tmp_m, date = queue.popleft()

        for i in range(6):
            nh = tmp_h + dh[i]
            nn = tmp_n + dn[i]
            nm = tmp_m + dm[i]

            # 안 익은 토마토라면 queue에 추가
            if (0 <= nh < H) and (0 <= nn < N) and (0 <= nm < M) and (tomato[nh][nn][nm] == 0):
                queue.append([nh, nn, nm, date + 1])
                tomato[nh][nn][nm] = 1

    # 모두 익었는지 확인
    if check():
        return date
    else:
        return -1
    

M, N, H = map(int, input().split())

# 토마토 상태 입력받기
tomato = [[[0]*M for n in range(N)] for h in range(H)]

for h in range(H):
    for n in range(N):
        tomato[h][n] = list(map(int, input().split()))

# 처음부터 다 익어있는지 확인
if check():
    print(0)
else:
    print(solve())
