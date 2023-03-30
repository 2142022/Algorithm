import sys
input = sys.stdin.readline

# 테스트케이스 개수
T = int(input())

# T개의 테스트케이스
for _ in range(T):
    # 수첩1의 정수의 개수
    N = int(input())

    # 수첩1의 정수
    diary1 = set(map(int, input().split()))

    # 수첩2의 정수의 개수
    M = int(input())

    # 수첩2의 정수
    diary2 = list(map(int, input().split()))

    # 수첩2의 정수들이 수첩1에 있는지 확인
    for i in range(M):
        if diary2[i] in diary1:
            print(1)
        else:
            print(0)
