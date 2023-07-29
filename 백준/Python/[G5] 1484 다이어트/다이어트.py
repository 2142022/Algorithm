import sys
input = sys.stdin.readline

# 현재 몸무게의 제곱 - 이전 몸무게의 제곱
G = int(input())

# 가능한 현재 몸무게의 개수
cnt = 0

# a^2 - b^2 = (a+b)(a-b) = G
# a + b가 G 이하여야 하므로 a(현재 몸무게)가 최대 G - 1까지만 확인
for i in range(2, G):
    for j in range(i - 1, 0, -1):
        # 현재 몸무게의 제곱 - 이전 몸무게의 제곱
        t = (i + j) * (i - j)

        # 현재 몸무게의 제곱 - 이전 몸무게의 제곱이 G 보다 크다면 끝내기
        if t > G:
            break
        # 현재 몸무게의 제곱 - 이전 몸무게의 제곱 = G인 경우
        elif t == G:
            print(i)
            cnt += 1

# 가능한 몸무게가 없는 경우
if cnt == 0:
    print(-1)