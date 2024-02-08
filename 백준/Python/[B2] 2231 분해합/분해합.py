import sys
input = sys.stdin.readline

# x의 생성자 구하기
def find(x):
    # 생성자
    num = 1
    while num < x:
        # 분해합
        s = num
        for i in str(num):
            s += int(i)

        # 생성자인 경우
        if s == x:
            return num
        num += 1

    # 생성자가 없는 경우
    return 0

################################333

# 자연수
N = int(input())

# N의 생성자 구하기
print(find(N))