import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 농장의 크기
    N = int(input())

    # 총 수익
    values = 0

    # 마름모 형태 중 위의 삼각형 수익 구하기
    # cnt: 탐색 행에서 수확하는 농작물의 개수
    # i: 탐색 행에서 수확하는 농작물의 시작
    cnt = 1
    for i in range(N // 2, -1, -1):
        # 행 정보 입력받기
        info = input().rstrip()
        for j in range(i, i + cnt):
            values += int(info[j])

        cnt += 2

    # 마름모 형태 중 아래 삼각형 수익 구하기
    cnt -= 4
    for i in range(1, N // 2 + 1):
        info = input().rstrip()
        for j in range(i, i + cnt):
            values += int(info[j])

        cnt -= 2

    print(f'#{t} {values}')
