import sys
input = sys.stdin.readline

# 에너지 드링크 수
N = int(input())

# 각 에너지 드링크의 양
x = list(map(int, input().split()))

# 오름차순 정렬
x.sort()

# 페인이 마실 수 있는 최대 에너지 드링크의 양
result = 0

# 맨 마지막 에너지 드링크(양이 가장 많은 에너지 드링크)를 제외하고 모두 더하기
for i in range(N - 1):
    result += x[i]

# 맨 마지막 에너지 드링크(양이 가장 많은 에너지 드링크)를 제외하고 모두 반으로 나누기
# 홀수인 경우 소수점도 구하기
if result % 2 == 0:
    result //= 2
else:
    result /= 2

# 맨 마지막 에너지 드링크(양이 가장 많은 에너지 드링크) 더하기
result += x[N - 1]

print(result)