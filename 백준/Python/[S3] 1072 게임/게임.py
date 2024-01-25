import sys
input = sys.stdin.readline

# 게임 횟수, 이긴 게임
X, Y = map(int, input().split())

# 현재 승률
Z = Y * 100 // X

# 승률이 변하는 횟수의 시작점과 끝점
start, end = 0, X

# 추가 게임 횟수를 반으로 줄여가면서 승률이 변하는지 체크
while start != end:
    middle = (start + end) // 2
    if (Y + middle) * 100 // (X + middle) != Z:
        end = middle
    else:
        start = middle + 1

# 절대 승률이 변하지 않는 경우
if (Y + start) * 100 // (X + end) == Z:
    print(-1)
else:
    print(start)

