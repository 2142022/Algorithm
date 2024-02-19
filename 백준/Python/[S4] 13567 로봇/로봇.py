import sys
input = sys.stdin.readline

# 명령어 수행
def perform():
    # 사방 탐색용
    dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

    # 현재 위치, 진행 방향
    r, c, d = 0, 0, 1

    # 명령어
    for _ in range(n):
        op, num = input().split()
        num = int(num)

        # 이동
        if op == 'MOVE':
            r += dr[d] * num
            c += dc[d] * num

            # 범위를 벗어난 경우
            if not (0 <= r <= M and 0 <= c <= M):
                return -1,

        # 회전
        else:
            if num == 0:
                d = (d + 1) % 4
            else:
                d = (d - 1) % 4

    return c, r

###############################################################

# 정사각형 S의 크기, 수행할 명령어 수
M, n = map(int, input().split())

# 명령어 수행 결과
res = perform()

# 명령어 열이 유효하지 않은 경우
if res[0] == -1:
    print(-1)
else:
    print(*res)