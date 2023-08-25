import sys
input = sys.stdin.readline

# 테스트케이스 개수
T = int(input())

# T개의 테스트케이스
for t in range(1, T + 1):
    # 두 정수
    A, B = map(int, input().split())

    # A+B의 값 출력
    print('Case #' + str(t) + ': ' + str(A + B))