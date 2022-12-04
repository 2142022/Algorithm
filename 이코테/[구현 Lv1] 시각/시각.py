import sys

input = sys.stdin.readline

# 00시 00분 00초 ~ N시 59분 59초 사이에 3이 하나라도 포함되는 모든 경우의 수 구하기
N = int(input())

# 시간에 3이 없는 경우의 수: 분에 3이 있는 경우의 수(15 * 60) + 분에 3이 없고 초에 3이 있는 경우의 수((60 - 15) * 15
# 분이나 초에 3이 있는 경우의 수는 15가지 (3, 13, 23, 30 ~ 39, 43, 53)
not_contain = 15 * 60 + 45 * 15

# 시간에 3이 있는 경우의 수: 60 * 60 (분, 초 모두 0 ~ 59 가능)
contain = 60 * 60

# 0 ~ 2시 (시간에 3이 있는 경우의 수: 0가지)
if N < 3:
    print((N + 1) * not_contain)
# 3 ~ 12시 (시간에 3이 있는 경우의 수: 1가지)
elif N < 13:
    print(contain + N * not_contain)
# 13 ~ 22시 (시간에 3이 있는 경우의 수: 2가지)
elif N < 23:
    print(2 * contain + (N - 1) * not_contain)
# 23시 (시간에 3이 있는 경우의 수: 3가지
else:
    print(3 * contain + (N - 2) * not_contain)
