from collections import  Counter
import sys
input = sys.stdin.readline

# 원래 문자열에서 각 문자의 개수
cnt = dict(Counter(input().rstrip()))

# 개수가 홀수인 문자가 여러개인 경우 팰린드롬 불가
if len(list(filter(lambda x: x % 2 == 1, cnt.values()))) > 1:
    print("I'm Sorry Hansoo")
    exit()

# 팰린드롬 앞부부, 중간, 뒷부분
front = middle = back = ''

# 알파벳 순서대로 추가
for alpha, cnt in sorted(list(cnt.items()), key = lambda x: x[0]):
    m, d = divmod(cnt, 2)

    # 중간 문자
    if d == 1:
        middle = alpha

    # 팰린드롬 추가
    front += alpha * m
    back = alpha * m + back

print(front + middle + back)