import sys
input = sys.stdin.readline

# 계단 수
N = int(input())

# 계단 점수
stairs = [int(input()) for _ in range(N)]

# score[i][0]: i 계단을 밟지 않은 경우
# score[i][1]: i-2 계단을 밟지 않고 i-1, i 계단을 밟은 경우
# score[i][2]: i-1 계단을 밟지 않고 i-2, i 계단을 밟은 경우
score = [[0] * 3 for _ in range(N)]
score[0] = [0, stairs[0], stairs[0]]
if N >= 2:
    score[1] = [stairs[0], stairs[0] + stairs[1], stairs[1]]
for i in range(2, N):
    # 현재 계단을 밟지 않기 위해서는 이전 계단을 무조건 밟아야 함
    score[i][0] = max(score[i - 1][1], score[i - 1][2])

    # 현재 계단을 밟고 이전 계단을 밟기 위해서는 2번째 전 계단을 밟지 않아야 함
    score[i][1] = score[i - 2][0] + stairs[i - 1] + stairs[i]

    # 현재 계단을 밟고 이전 계단을 밟지 않기 위해서는 2번째 전 계단을 무조건 밟아야 함
    score[i][2] = max(score[i - 2][1], score[i - 2][2]) + stairs[i]

print(max(score[N - 1][1], score[N - 1][2]))