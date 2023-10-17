import sys
input = sys.stdin.readline

# 입력받는 수의 자릿수, 지울 수 있는 숫자의 개수
N, K = map(int, input().split())

# 수
nums = input().rstrip()

# 최종 숫자
result = []

# 숫자 하나씩 탐색
for num in nums:
    # 현재 숫자보다 작은 숫자가 앞에 있다면, 작은 숫자 삭제
    # 단, K개까지만 삭제 가능
    while K and result and result[-1] < num:
        result.pop()
        K -= 1

    # 현재 숫자 추가
    result.append(num)

# K개를 모두 삭제하지 않은 경우, 뒤의 K개 삭제
if K:
    print(''.join(result[:-K]))
else:
    print(''.join(result))