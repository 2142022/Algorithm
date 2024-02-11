import sys
input = sys.stdin.readline

# 삼각형 크기
n = int(input())

# 각 위치에서의 경로의 최대 합
s = [[0] * n for _ in range(n)]
s[0][0] = int(input())

# 두 번째 줄부터 입력받기
for i in range(1, n):
    # 입력받은 행
    row = list(map(int, input().split()))

    # 왼쪽 대각선과 오른쪽 대각선을 비교하여 최대와 더하기
    for j in range(i + 1):
        # 0열
        if j == 0:
            s[i][j] = s[i - 1][j] + row[j]
        # 마지막 열
        elif j == i:
            s[i][j] = s[i - 1][j - 1] + row[j]
        # 가운데 열
        else:
            s[i][j] = max(s[i - 1][j - 1], s[i - 1][j]) + row[j]

print(max(s[-1]))
