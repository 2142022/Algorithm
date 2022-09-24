import sys
input = sys.stdin.readline

# 전선을 놓을 수 있는지 체크
def check(status, r, c, case):
    # 상
    if case == 1:
        for i in range(0, r):
            if status[i][c] == 1:
                return False
        return True

    # 하
    elif case == 2:
        for i in range(r + 1, N):
            if status[i][c] == 1:
                return False
        return True

    # 좌
    elif case == 3:
        for i in range(0, c):
            if status[r][i] == 1:
                return False
        return True

    # 우
    elif case == 4:
        for i in range(c + 1, N):
            if status[r][i] == 1:
                return False
        return True
    
#################################################################

# idx: core의 인덱스
# cnt: 현재까지 전원에 연결한 core의 개수
# length: 현재까지의 전선 길이 합
def solve(status, idx, cnt, length):
    global max_core, min_sum
    
    # core를 모두 확인하면 끝내기
    if idx == len(core):
        # 현재까지 전원에 연결한 core의 개수가 max_core보다 크면 min_sum 바꾸기
        if cnt > max_core:
            max_core = cnt
            min_sum = length

        # 현재까지 전원에 연결한 core의 개수가 max_core와 같다면 값 비교
        elif cnt == max_core:
            min_sum = min(length, min_sum)

        return

    # 가장 자리에 위치한 core는 이미 전원이 연결되어 있으므로 패스
    if core[idx][0] == 0 or core[idx][0] == N - 1 or core[idx][1] == 0 or core[idx][1] == N - 1:
        solve(status, idx + 1, cnt + 1, length)
        
    else:
        # 위로 전선을 놓을 수 있는 경우
        if check(status, core[idx][0], core[idx][1], 1):
            tmp = [[0] * N for i in range(N)]
            for i in range(N):
                for j in range(N):
                    if j == core[idx][1] and i < core[idx][0]:
                        tmp[i][j] = 1
                    else:
                        tmp[i][j] = status[i][j]

            solve(tmp, idx + 1, cnt + 1, length + core[idx][0])

        # 아래로 전선을 놓을 수 있는 경우
        if check(status, core[idx][0], core[idx][1], 2):
            tmp = [[0] * N for i in range(N)]
            for i in range(N):
                for j in range(N):
                    if j == core[idx][1] and i > core[idx][0]:
                        tmp[i][j] = 1
                    else:
                        tmp[i][j] = status[i][j]

            solve(tmp, idx + 1, cnt + 1, length + N - 1 - core[idx][0])

        # 왼쪽으로 전선을 놓을 수 있는 경우
        if check(status, core[idx][0], core[idx][1], 3):
            tmp = [[0] * N for i in range(N)]
            for i in range(N):
                for j in range(N):
                    if i == core[idx][0] and j < core[idx][1]:
                        tmp[i][j] = 1
                    else:
                        tmp[i][j] = status[i][j]

            solve(tmp, idx + 1, cnt + 1, length + core[idx][1])

        # 오른쪽으로 전선을 놓을 수 있는 경우
        if check(status, core[idx][0], core[idx][1], 4):
            tmp = [[0] * N for i in range(N)]
            for i in range(N):
                for j in range(N):
                    if i == core[idx][0] and j > core[idx][1]:
                        tmp[i][j] = 1
                    else:
                        tmp[i][j] = status[i][j]

            solve(tmp, idx + 1, cnt + 1, length + N - 1 - core[idx][1])

        # 전선을 놓지 않고 패스
        solve(status, idx + 1, cnt, length)


#####################################################################    

# 테스트케이스 개수
T = int(input())

# T개의 테스트케이스
for t in range(1, T + 1):
    # cell 판의 크기
    N = int(input())

    # cell 판의 정보
    cell = [list(map(int, input().split())) for i in range(N)]

    # core의 위치
    core = []
    for i in range(N):
        for j in range(N):
            if cell[i][j] == 1:
                core.append([i, j])

    # 전원에 연결된 최대 core의 개수
    max_core = 0

    # 최소 전선 길이 합
    min_sum = N * N

    solve(cell, 0, 0, 0)

    print("#" + str(t) + " " + str(min_sum))
