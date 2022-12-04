import sys
input = sys.stdin.readline

# 현재 캐릭터의 점수 (문자열로 입력받기)
N = input().strip()

# 점수의 자릿수
length = len(N)

# 자릿수의 반
half_len = length // 2

# 앞자리 숫자들의 합
front_sum = 0
# 뒷자리 숫자들의 합
back_sum = 0

for i in range(length):
    # 앞자리 숫자들 더하기
    if i < half_len:
        front_sum += int(N[i])
    # 뒷자리 숫자들 더하기
    else:
        back_sum += int(N[i])

# 앞자리 숫자들의 합과 뒷자리 숫자들의 합이 같다면 LUCKY, 아니면 READY
if front_sum == back_sum:
    print('LUCKY')
else:
    print('READY')