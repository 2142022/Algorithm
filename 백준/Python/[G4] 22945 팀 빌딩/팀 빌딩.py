import sys
input = sys.stdin.readline

# 개발자 수
N = int(input())

# 개발자의 능력치
x = list(map(int, input().split()))

# 팀의 최대 능력치
result = 0
# 시작, 마지막 팀원
start, end = 0, N - 1

# 시작 팀원과 마지막 팀원 사이에 개발자가 1명 있을 때까지 반복
while start + 1 < end:
    result = max(result, (end - start - 1) * min(x[start], x[end]))

    # 시작 팀원과 마지막 팀원 중, 더 적은 능력치를 가진 팀원을 배제
    if x[start] < x[end]:
        start += 1
    else:
        end -= 1

print(result)