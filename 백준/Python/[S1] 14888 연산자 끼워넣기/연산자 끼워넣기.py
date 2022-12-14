import sys
input = sys.stdin.readline
from itertools import permutations

# 계산하는 함수
def calculate(num1, op, num2):
    # 덧셈
    if op == 0:
        return num1 + num2
    # 뺄셈
    elif op == 1:
        return num1 - num2
    # 곱셈
    elif op == 2:
        return num1 * num2
    # 나눗셈
    else:
        # num1이 음수인 경우
        # num1을 양수로 바꾼 뒤 몫을 구하고, 그 몫을 음수로 바꾸기
        if num1 < 0:
            return (-1) * (abs(num1) // num2)
        else:
            return num1 // num2

#################################################################

# 수의 개수
N = int(input().strip())

# N개의 수를 담은 리스트
nums = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈의 개수를 담은 리스트
operator_cnt = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈을 개수만큼 담은 리스트
operators = []
for i in range(4):
    if operator_cnt[i] != 0:
        for _ in range(operator_cnt[i]):
            operators.append(i)

# 결과의 최대값
max_result = -2147483648
# 결과의 최소값
min_result = 2147483647

# operators의 순열을 이용하여 식 구하기
for ops in permutations(operators, N - 1):
    # 현재 식의 결과값
    # 첫 번째 수로 초기화
    result = nums[0]

    # 식 계산하기
    # (수의 개수 - 1)만큼 반복
    for i in range(N - 1):
        result = calculate(result, ops[i], nums[i + 1])

    # 최대값, 최소값 비교하기
    max_result = max(result, max_result)
    min_result = min(result, min_result)

# 최대값, 최소값 출력
print(max_result)
print(min_result)