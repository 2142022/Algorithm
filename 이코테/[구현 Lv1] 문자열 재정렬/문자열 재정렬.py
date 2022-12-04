import sys
input = sys.stdin.readline

# 문자열을 배열로 입력받기
string = list(input().strip())

# 숫자들의 합
num_sum = 0

# 숫자들은 pop을 통해 더하고 문자열에서 삭제
# pop을 하면 문자열 길이가 줄어드므로 뒤에서부터 탐색
for i in range(len(string) - 1, -1, -1):
    # 아스키코드를 이용해 숫자인지 확인
    if ord('0') <= ord(string[i]) <= ord('9'):
        num_sum += int(string.pop(i))

# 남은 문자열 오름차순 정렬
string.sort()

# 배열을 문자열로 변환 후 숫자합과 함께 출력
# 숫자합이 0인 경우는 문자열만 출력
if num_sum != 0:
    print(''.join(string) + str(num_sum))
else:
    print(''.join(string))