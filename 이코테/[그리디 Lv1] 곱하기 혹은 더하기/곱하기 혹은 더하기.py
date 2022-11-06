import sys
input = sys.stdin.readline

# 문자열 입력받기
S = input().strip()

# 결과 값: 첫 숫자로 초기화
result = int(S[0])

for i in range(1, len(S)):
    # 결과값이 0이거나 1, 혹은 현재 값이 0이거나 1인 경우에는 더하기
    num = int(S[i])

    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)