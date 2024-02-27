from collections import defaultdict
import sys
input = sys.stdin.readline

# x가 답이 될 수 있는지 확인
def possible(x):
    x = str(x)

    # 동일한 숫자가 있는 경우 패스
    if len(set(x)) != 3:
        return False

    # 0이 있으면 안 됨
    if '0' in x:
        return False

    # 질문에 대한 답과 비교
    for q, a in question.items():
        q = str(q)

        # 스트라이크, 볼의 개수
        s = b = 0
        for i in range(3):
            if x[i] == q[i]:
                s += 1
            elif x[i] in q:
                b += 1

        # 질문에 대한 답과 다른 경우
        if (s, b) != a:
            return False

    return True

##################################################

# 질문 횟수
N = int(input())

# 각 질문에 대한 대답
question = defaultdict(tuple)
for _ in range(N):
    num, s, b = map(int, input().split())
    question[num] = (s, b)

# 답이 될 수 있는 수의 개수
cnt = 0

# 100 ~ 999 모두 검사
for num in range(123, 988):
    # num이 답이 될 수 있는지 확인
    if possible(num):
        cnt += 1

print(cnt)