import sys
input = sys.stdin.readline

# 현재 경계 내에서의 인구수 차이 구하기
def get_diff():
    # 선거구1
    one = 0
    for i in range(r):
        for j in range(c + 1):
            one += A[i][j]
    t = 0
    for i in range(r, r + d1):
        for j in range(c - t):
            one += A[i][j]
        t += 1

    # 인구가 없으면 끝
    if not one:
        return diff

    # 가장 많은 인구수, 적은 인구수
    max_cnt, min_cnt = one, one

    # 선거구2
    two = 0
    for i in range(r):
        for j in range(c + 1, N):
            two += A[i][j]
    t = 0
    for i in range(r, r + d2 + 1):
        for j in range(c + 1 + t, N):
            two += A[i][j]
        t += 1

    # 인구가 없으면 끝
    if not two:
        return diff
    max_cnt = max(max_cnt, two)
    min_cnt = min(min_cnt, two)

    # 선거구3
    three = 0
    t = 0
    for i in range(r + d1, r + d1 + d2 + 1):
        for j in range(c - d1 + t):
            three += A[i][j]
        t += 1
    for i in range(r + d1 + d2 + 1, N):
        for j in range(c - d1 + d2):
            three += A[i][j]

    # 인구가 없으면 끝
    if not three:
        return diff
    max_cnt = max(max_cnt, three)
    min_cnt = min(min_cnt, three)

    # 선거구4
    four = 0
    t = 0
    for i in range(r + d2 + 1, r + d1 + d2 + 1):
        for j in range(c + d2 - t, N):
            four += A[i][j]
        t += 1
    for i in range(r + d1 + d2 + 1, N):
        for j in range(c - d1 + d2, N):
            four += A[i][j]

    # 인구가 없으면 끝
    if not four:
        return diff
    max_cnt = max(max_cnt, four)
    min_cnt = min(min_cnt, four)

    # 선거구5
    five = total - one - two - three - four

    # 인구가 없으면 끝
    if not five:
        return diff
    max_cnt = max(max_cnt, five)
    min_cnt = min(min_cnt, five)

    return max_cnt - min_cnt

###################################################################

# 재현시 크기
N = int(input())

# 각 구역의 인구 수
A = []

# 총 인구수
total = 0
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)
    total += sum(row)

# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값
diff = total

# 기준점
for r in range(N):
    for c in range(N):
        # 경계선
        d1 = 0
        while r + d1 < N and c - d1 >= 0:
            d2 = 0
            while r + d1 + d2 < N and c + d2 < N:
                # 현재 경계 내에서의 인구수 차이 구하기
                diff = min(diff, get_diff())
                d2 += 1
            d1 += 1

print(diff)