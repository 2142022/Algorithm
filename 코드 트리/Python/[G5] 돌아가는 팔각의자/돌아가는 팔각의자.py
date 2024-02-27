import sys
input = sys.stdin.readline

# 함께 회전할 의자 번호와 방향 구하기
# N: 회전하는 기준 의자
# D: 기준 의자가 회전하는 방향
def find_who(N, D):
    # 왼쪽 의자 탐색
    i, j = N, N - 1
    d = D
    while j >= 0:
        # 인접한 두 사람이 같은 지역인 경우 회전 X
        if chairs[i][(idx[i] - 2) % 8] == chairs[j][(idx[j] + 2) % 8]:
            break

        # 회전할 의자에 추가
        together.append((j, -d))
        i, j = j, j - 1
        d *= -1

    # 오른쪽 의자 탐색
    i, j = N, N + 1
    d = D
    while j < 4:
        # 인접한 두 사람이 같은 지역인 경우 회전 X
        if chairs[i][(idx[i] + 2) % 8] == chairs[j][(idx[j] - 2) % 8]:
            break

        # 회전할 의자에 추가
        together.append((j, -d))
        i, j = j, j + 1
        d *= -1

############################################################################

# 각 의자에 앉아있는 사람들의 지역
chairs = [list(map(int, input().rstrip())) for _ in range(4)]

# 각 의자에서 12시 방향을 가리키는 사람의 번호
idx = [0] * 4

# 의자 회전
for _ in range(int(input())):
    # 회전시킬 팔각의자 번호, 방향
    n, d = map(int, input().split())
    n -= 1

    # 함께 회전할 의자 번호와 방향
    together = [(n, d)]
    find_who(n, d)

    # 함께 회전하는 의자 모두 회전
    for x, y in together:
        idx[x] = (idx[x] - y) % 8

# 12시 방향에 남쪽지방 사람 착석여부 (1*s1 + 2*s2 + 4*s3 + 8*s4)
result = 0
for i in range(4):
    result += 2 ** i * chairs[i][idx[i]]

print(result)