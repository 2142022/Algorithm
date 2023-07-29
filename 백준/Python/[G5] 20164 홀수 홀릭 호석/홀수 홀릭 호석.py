from itertools import combinations
import sys
input = sys.stdin.readline

# 홀수 개수 반환
def count_odd(N):
    # 홀수 개수
    cnt = 0

    # 한 숫자씩 홀수인지 확인
    for i in range(len(N)):
        if int(N[i]) % 2 == 1:
            cnt += 1

    return cnt

############################################################################

# 현재 수를 나눠서 규칙대로 연산하기
# n: 현재 수
# p: 현재 수를 나눌 인덱스들
# cnt: 현재까지의 홀수 개수
def cal(n, p, cnt):
    # 현재 수를 나누고 더한 값
    result = 0

    # 두 자리 수인 경우
    if len(p) == 1:
        result = int(n[:p[0]]) + int(n[p[0]:])
    # 세 자리 수인 경우
    else:
        result = int(n[:p[0]]) + int(n[p[0]:p[1]]) + int(n[p[1]:])

    # 결과값을 문자로 변환
    s = str(result)
    # 결과값의 홀수 개수 구하기
    result_cnt = count_odd(s)

    # 결과값이 한 자리 수라면 끝내기
    if len(s) == 1:
        global min_result, max_result

        min_result = min(min_result, cnt + result_cnt)
        max_result = max(max_result, cnt + result_cnt)

    # 결과값이 두 자리 수라면 p = [1]로 재귀
    elif len(s) == 2:
        cal(s, [1], cnt + result_cnt)

    # 결과값이 세 자리 수 이상인 수들은 재귀
    else:
        for c in list(combinations([i for i in range(1, len(s))], 2)):
            cal(s, c, cnt + result_cnt)

############################################################################

# 호석이가 가지고 있는 수
N = input().rstrip()

# 최소 최종값
min_result = 2147483647
# 최대 최종값
max_result = 0
# 현재까지의 홀수 개수
cnt = count_odd(N)

# 한 자리 수의 경우, 최소 최종값과 최대 최종값이 cnt와 같음
if len(N) == 1:
    min_result = max_result = cnt
# 두 자리 수의 경우, 2개의 숫자로 분리하여 연산
elif len(N) == 2:
    cal(N, [1], cnt)
# 세 자리 이상인 수의 경우, 3개의 숫자로 분리하여 연산
elif len(N) >= 3:
    for c in list(combinations([i for i in range(1, len(N))], 2)):
        cal(N, c, cnt)

print(min_result, max_result)