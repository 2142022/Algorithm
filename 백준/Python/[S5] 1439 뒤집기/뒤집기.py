import sys
input = sys.stdin.readline

# 입력받은 문자열
S = input().strip()

# 이전 숫자와 다르다면 +1
cnt = 0

for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        cnt += 1

# 숫자가 바뀐 횟수가 홀수라면 2로 나눈 후 +1, 짝수라면 2로 나누기
if cnt % 2 == 1:
    print(cnt // 2 + 1)
else:
    print(cnt // 2)