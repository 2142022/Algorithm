from collections import defaultdict
import sys
input = sys.stdin.readline

# 음의 수, 프렛 수
N, P = map(int, input().split())

# 각 줄별로 누르고 있는 프렛 번호를 담은 스택
stack = defaultdict(list)

# 손가락을 움직이는 최소 횟수
cnt = 0

for i in range(N):
    # 눌러야 하는 줄과 프렛 번호
    string, fret = map(int, input().split())

    # 이미 누르고 있는 손가락을 떼야만 하는 경우
    while stack[string] and stack[string][-1] > fret:
        stack[string].pop()
        cnt += 1

    # 이미 눌러야 하는 곳을 누르고 있다면 패스
    if stack[string] and stack[string][-1] == fret:
        continue

    # 누르기
    stack[string].append(fret)
    cnt += 1

print(cnt)