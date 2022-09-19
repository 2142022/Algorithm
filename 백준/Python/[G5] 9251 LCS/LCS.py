import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

# (str2 길이 + 1) X (str1 길이 + 1)
dp = [[0] * (len(str1) + 1) for i in range(len(str2) + 1)]

for i in range(len(str2)):
    for j in range(len(str1)):
        # 같은 문자가 나온 경우 이전 값 + 1
        if str2[i] == str1[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        # 그 외에는 왼쪽 값과 위쪽 값 비교
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(dp[-1][-1])
