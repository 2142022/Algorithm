import copy
import sys
input = sys.stdin.readline

# 1번 연산: 각 부분 배열 상하 반전
# l: 연산 단계
def op1(l):
    global N

    # 한 행당 존재하는 부분 배열의 개수
    x = 2 ** (N - l)
    # 각 부분 배열의 크기
    y = 2 ** l

    # 상하 반전
    for i in range(x):
        for j in range(y // 2):
              arr[i * y + j], arr[(i + 1) * y - 1 - j] = arr[(i + 1) * y - 1 - j], arr[i * y + j]

####################################################################################################################

# 2번 연산: 각 부분 배열 좌우 반전
# l: 연산 단계
def op2(l):
    global N

    # 한 행당 존재하는 부분 배열의 개수
    x = 2 ** (N - l)
    # 각 부분 배열의 크기
    y = 2 ** l

    # 좌우 반전
    for i in range(2 ** N):
        for j in range(x):
            for k in range(y // 2):
                arr[i][j * y + k], arr[i][(j + 1) * y - 1 - k] = arr[i][(j + 1) * y - 1 - k], arr[i][j * y + k]

####################################################################################################################

# 3번 연산: 각 부분 배열 시계 방향으로 90도 회전
# l: 연산 단계
def op3(l):
    global N

    # 한 행당 존재하는 부분 배열의 개수
    x = 2 ** (N - l)
    # 각 부분 배열의 크기
    y = 2 ** l

    # 배열 복사본
    clone = copy.deepcopy(arr)

    # 시계 방향으로 90도 회전
    for i in range(x):
        for j in range(x):
            for m in range(y):
                for n in range(y):
                    arr[i * y + n][(j + 1) * y - 1 - m] = clone[i * y + m][j * y + n]

####################################################################################################################

# 4번 연산: 각 부분 배열 시계 반대 방향으로 90도 회전
# l: 연산 단계
def op4(l):
    global N

    # 한 행당 존재하는 부분 배열의 개수
    x = 2 ** (N - l)
    # 각 부분 배열의 크기
    y = 2 ** l

    # 배열 복사본
    clone = copy.deepcopy(arr)

    # 시계 반대 방향으로 90도 회전
    for i in range(x):
        for j in range(x):
            for m in range(y):
                for n in range(y):
                    arr[(i + 1) * y - 1 - n][j * y + m] = clone[i * y + m][j * y + n]

####################################################################################################################

# 5번 연산: 부분 배열끼리 상하 반전 (부분 배열의 내부는 변화X)
# l: 연산 단계
def op5(l):
    global N

    # 한 행당 존재하는 부분 배열의 개수
    x = 2 ** (N - l)
    # 각 부분 배열의 크기
    y = 2 ** l

    # 부분 배열끼리 상하 반전 (부분 배열의 내부는 변화X)
    for i in range(x // 2):
        for j in range(y):
            arr[i * y + j], arr[(x - 1 - i) * y + j] = arr[(x - 1 - i) * y + j], arr[i * y + j]

####################################################################################################################

# 6번 연산: 부분 배열끼리 좌우 반전 (부분 배열의 내부는 변화X)
# l: 연산 단계
def op6(l):
    global N

    # 한 행당 존재하는 부분 배열의 개수
    x = 2 ** (N - l)
    # 각 부분 배열의 크기
    y = 2 ** l

    # 부분 배열끼리 좌우 반전 (부분 배열의 내부는 변화X)
    for i in range(2 ** N):
        for j in range(x // 2):
            for k in range(y):
                arr[i][j * y + k], arr[i][(x - 1 - j) * y + k] = arr[i][(x - 1 - j) * y + k], arr[i][j * y + k]

####################################################################################################################

# 7번 연산: 부분 배열끼리 시계 방향으로 90도 회전 (부분 배열의 내부는 변화X)
# l: 연산 단계
def op7(l):
    global N

    # 한 행당 존재하는 부분 배열의 개수
    x = 2 ** (N - l)
    # 각 부분 배열의 크기
    y = 2 ** l

    # 배열 복사본
    clone = copy.deepcopy(arr)

    # 부분 배열끼리 시계 방향으로 90도 회전 (부분 배열의 내부는 변화X)
    for i in range(x):
        for j in range(x):
            for m in range(y):
                for n in range(y):
                    arr[j * y + m][(x - 1 - i) * y + n] = clone[i * y + m][j * y + n]

####################################################################################################################

# 8번 연산: 부분 배열끼리 시계 반대 방향으로 90도 회전 (부분 배열의 내부는 변화X)
# l: 연산 단계
def op8(l):
    global N

    # 한 행당 존재하는 부분 배열의 개수
    x = 2 ** (N - l)
    # 각 부분 배열의 크기
    y = 2 ** l

    # 배열 복사본
    clone = copy.deepcopy(arr)

    # 부분 배열끼리 시계 반대 방향으로 90도 회전 (부분 배열의 내부는 변화X)
    for i in range(x):
        for j in range(x):
            for m in range(y):
                for n in range(y):
                    arr[(x - 1 - j) * y + m][i * y + n] = clone[i * y + m][j * y + n]

####################################################################################################################

# N: 배열의 크기, R: 연산 횟수
N, R = map(int, input().split())

# 배열
arr = [list(map(int, input().split())) for _ in range(2 ** N)]

# R번의 연산
for _ in range(R):
    # k: 연산 종류, l: 연산 단계
    k, l = map(int, input().split())

    if k == 1 and l > 0:
        op1(l)
    elif k == 2 and l > 0:
        op2(l)
    elif k == 3 and l > 0:
        op3(l)
    elif k == 4 and l > 0:
        op4(l)
    elif k == 5:
        op5(l)
    elif k == 6:
        op6(l)
    elif k == 7:
        op7(l)
    elif k == 8:
        op8(l)

# 배열 출력
for i in range(2 ** N):
    for j in range(2 ** N):
        print(arr[i][j], end = ' ')
    print()