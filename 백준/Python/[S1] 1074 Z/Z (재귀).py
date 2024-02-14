import sys
input = sys.stdin.readline

# 이동 횟수 구하기
# (r, c): 탐색 범위의 시작 위치
# n: 탐색 구간 크기의 반
def get_cnt(r, c, n):
    # 더 이상 분할할 수 없는 경우 끝내기
    if n == 0:
        return 1

    # 탐색 구간을 4분면으로 나눴을 때 목표 위치 찾기
    if R < r + n:
        if C < c + n:
            return get_cnt(r, c, n // 2)
        else:
            return n * n + get_cnt(r, c + n, n // 2)
    else:
        if C < c + n:
            return 2 * n * n + get_cnt(r + n, c, n // 2)
        else:
            return 3 * n * n + get_cnt(r + n, c + n, n // 2)

########################################################################

# 배열 크기, 목표 위치
N, R, C = map(int, input().split())

# 이동 횟수 구하기 (첫 위치는 세지 않으므로 -1)
print(get_cnt(0, 0, 2 ** (N - 1)) - 1)
