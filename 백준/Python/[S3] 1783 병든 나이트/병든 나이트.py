import sys
input = sys.stdin.readline

# 체스판 크기
N, M = map(int, input().split())

# 세로가 1인 경우 움직일 수 없음
if N == 1:
    print(1)

# 세로가 2인 경우, 2번과 3번만 가능
elif N == 2:
    print(min((M - 1) // 2 + 1, 4))

# 세로가 3 이상인 경우
else:
    # 가로가 3이하인 경우
    if M <= 3:
        print(M)
    # 가로가 6이하인 경우
    elif M <= 6:
        print(4)
    # 가로가 7이하인 경우
    elif M <= 7:
        print(5)
    else:
        print(M - 2)
