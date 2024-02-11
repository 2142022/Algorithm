import sys
input = sys.stdin.readline

# 배열 크기, 최종 방문 위치
N, R, C = map(int, input().split())

# 최종 방문 횟수
cnt = 0

# 최종 위치가 있는 사각형의 시작점과 크기의 절반
r, c, l = 0, 0, 2 ** (N - 1)

while True:
    # 현재 위치가 최종 위치인 경우
    if r == R and c == C:
        print(cnt)
        break

    # 현재 탐색 사각형을 4분면으로 나눴을 때 최종 위치의 위치 찾기
    if r <= R < r + l and c <= C < c + l:
        l //= 2
    elif r <= R < r + l and c + l <= C < c + 2 * l:
        c += l
        cnt += l * l
        l //= 2
    elif r + l <= R < r + 2 * l and c <= C < c + l:
        r += l
        cnt += l * l * 2
        l //= 2
    else:
        r += l
        c += l
        cnt += l * l * 3
        l //= 2

