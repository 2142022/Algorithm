import sys
input = sys.stdin.readline

# 테스트 케이스
for _ in range(int(input())):
    # 스티커 가로 크기
    n = int(input())

    # 스티커 점수
    score = [list(map(int, input().split())) for _ in range(2)]

    # 스티커 가로 크기가 1개인 경우
    if n == 1:
        print(max(score[0][0], score[1][0]))
        continue

    # 한 열씩 스티커 점수 비교
    score[0][1] += score[1][0]
    score[1][1] += score[0][0]

    # 3번째 열부터 점수 비교
    for i in range(2, n):
        score[0][i] += max(score[1][i - 1], score[1][i - 2])
        score[1][i] += max(score[0][i - 1], score[0][i - 2])

    # 최대 스티커 점수
    print(max(score[0][-1], score[0][-2], score[1][-1], score[1][-2]))