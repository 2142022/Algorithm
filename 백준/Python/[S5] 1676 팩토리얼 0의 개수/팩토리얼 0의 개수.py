import sys
input = sys.stdin.readline

N = int(input())

# 0의 개수는 2 x 5의 쌍의 개수
# 2의 개수는 5의 개수보다 무조건 많으므로 5의 개수 세기
# 25 = 5x5, 125 = 5x5x5이므로 배수의 개수 더하기
print(N // 5 + N // 25 + N // 125)