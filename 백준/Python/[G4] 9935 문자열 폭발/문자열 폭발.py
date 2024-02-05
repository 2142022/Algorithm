import sys
input = sys.stdin.readline

# 원래 문자열
origin = input().rstrip()
# 폭발 문자열
remove = list(input().rstrip())

# 최종 문자열을 담은 스택
result = []
for c in origin:
    # 폭발 문자열의 마지막 글자인 경우, 폭발 문자열인지 확인한 후 스택에서 제거
    if c == remove[-1] and result[len(result) - len(remove) + 1:] == remove[:-1]:
        for i in range(len(remove) - 1):
            result.pop()
    else:
        result.append(c)

# 빈 문자열인 경우
if not result:
    print('FRULA')
else:
    print(''.join(result))