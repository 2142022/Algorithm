import sys
input = sys.stdin.readline

# 세 문자열
# DP에서 0행과 0열을 모두 공백으로 초기화하기 위해 앞에 공백 추가
s1 = ' ' + input().rstrip()
s2 = ' ' + input().rstrip()
s3 = ' ' + input().rstrip()

# 세 문자열의 LCS의 길이
lcs = [[[0] * len(s3) for _ in range(len(s2))] for _ in range(len(s1))]

# s1의 한 글자씩 탐색
for i in range(1, len(s1)):
    # s2의 한 글자씩 탐색:
    for j in range(1, len(s2)):
        # s3의 한 글자씩 탐색
        for k in range(1, len(s3)):
            # 세 문자열의 현재 글자가 같다면 기존 LCS 길이 +1
            if s1[i] == s2[j] and s2[j] == s3[k]:
                lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
            # 그 외에는 현재까지 가장 긴 LCS의 길이 저장
            else:
                lcs[i][j][k] = max(lcs[i - 1][j][k], lcs[i][j - 1][k], lcs[i][j][k - 1])

# 가장 긴 LCS의 길이 출력
print(lcs[-1][-1][-1])