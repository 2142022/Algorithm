import sys
input = sys.stdin.readline

# 두 문자열
# DP의 0행과 0열을 0으로 초기화시키기 위해 앞에 공백 추가
s1 = ' ' + input().rstrip()
s2 = ' ' + input().rstrip()

# 현재까지 가장 긴 부분 문자열
lcs = [[''] * len(s2) for _ in range(len(s1))]

# s1 한 글자씩 탐색
for i in range(1, len(s1)):
    # s2 한 글자씩 탐색
    for j in range(1, len(s2)):
        # s1과 s2의 문자가 같은 경우, lcs에 현재 문자 추가
        if s1[i] == s2[j]:
            lcs[i][j] = lcs[i - 1][j - 1] + s1[i]
        # s1과 s2의 문자가 다른 경우, 현재까지 가장 긴 문자열로 저장
        else:
            if len(lcs[i - 1][j]) >= len(lcs[i][j - 1]):
                lcs[i][j] = lcs[i - 1][j]
            else:
                lcs[i][j] = lcs[i][j - 1]

# 최종 LCS
s = lcs[-1][-1]

# LCS가 있는 경우에는 길이과 LCS 모두 출력
if len(s):
    print(len(s))
    print(s)
else:
    print(0)