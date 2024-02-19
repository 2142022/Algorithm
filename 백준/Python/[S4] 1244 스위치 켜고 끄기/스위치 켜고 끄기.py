import sys
input = sys.stdin.readline

# 남학생인 경우, x의 배수들의 스위치 바꾸기
def boy(x):
    for i in range(x, N + 1, x):
        on[i] ^= 1

#################################################################

# 여학생인 경우, x를 기준으로 좌우가 같은 최장 길이의 스위치 모두 바꾸기
def girl(x):
    diff = min(x - 1, N - x)
    for d in range(diff, -1, -1):
        # 좌우가 같은지 확인
        if on[x - d:x + d + 1] == on[x - d:x + d + 1][::-1]:
            # 스위치 모두 바꾸기
            for i in range(x - d, x + d + 1):
                on[i] ^= 1
            return

#################################################################

# 스위치 개수
N = int(input())

# 스위치 상태
on = [0] + list(map(int, input().split()))

# 학생
for _ in range(int(input())):
    # 성별, 받은 수
    sex, num = map(int, input().split())

    # 남학생인 경우
    if sex == 1:
        boy(num)

    # 여학생인 경우
    else:
        girl(num)

# 스위치 상태 출력
for i in range(1, N + 1, 20):
    print(*on[i:i + 20])