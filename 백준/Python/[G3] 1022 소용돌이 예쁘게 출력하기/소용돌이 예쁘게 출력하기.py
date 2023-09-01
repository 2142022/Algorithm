import sys
input = sys.stdin.readline

# (r1, c1): 출력할 행렬의 가장 왼쪽 위 칸
# (r2, c2): 출력할 행렬의 가장 오른쪽 아래 칸
r1, c1, r2, c2 = map(int, input().split())

# 출력해야 하는 행의 개수, 열의 개수
rc = r2 - r1 + 1
cc = c2 - c1 + 1

# 출력할 행렬
matrix = [[0] * (cc) for _ in range(rc)]

# 행렬의 최대값
max_num = 0

# 행렬 채우기
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        # 현재 위치가 몇 번째 사각형인지 구하기
        l = max(abs(i), abs(j)) + 1

        # l번째 사각형의 가장 왼쪽 위 숫자
        n = (2 * (l - 1)) ** 2 + 1

        # 현재 위치의 숫자
        num = n
        if j == -(l - 1) or i == l - 1:
            num = n + (i + l - 1) + (j + l - 1)
        else:
            num = n - (i + l - 1) - (j + l - 1)

        # 행렬 채우고 최대값 비교
        matrix[i - r1][j - c1] = num
        max_num = max(max_num, num)


# 원하는 부분 출력
for i in range(rc):
    for j in range(cc):
        print(f"{matrix[i][j]:{len(str(max_num))}d}", end = ' ')
    print()