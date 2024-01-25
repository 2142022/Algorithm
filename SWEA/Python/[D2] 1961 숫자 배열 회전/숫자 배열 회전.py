import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 행렬 크기
    N = int(input())

    # 원래 배열
    arr = [list(input().split()) for _ in range(N)]

    # 회전한 배열을 합한 모양
    result = [[''] * N for _ in range(N)]

    # 시계방향으로 90도씩 회전하기
    for j in range(3):
        arr = list(zip(*arr[::-1]))

        # 결과에 추가하기
        for i in range(N):
            result[i][j] += ''.join(arr[i])

    # 출력
    print(f'#{t}')
    for row in result:
        print(*row)