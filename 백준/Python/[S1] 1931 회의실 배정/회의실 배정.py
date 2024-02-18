import sys
input = sys.stdin.readline

# 회의 수
N = int(input())

# 회의 시간 (시작 시간 기준 오름차순 정렬 후, 종료 시간 기준 오름차순 정렬)
time = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: (x[0], x[1]))

# 최대 사용할 수 있는 회의 수
cnt = 0

# 마지막으로 선택한 회의의 끝나는 시간
last = 0

# 각 회의 탐색
for s, e in time:
    # 현재 회의가 마지막으로 선택한 회의보다 일찍 끝나는 경우 바꾸기
    # 어차피 시작 시간은 오름차순 정렬되어 있음
    if e < last:
        last = e

    # 마지막 회의에 이어서 할 수 있는 경우, 추가
    elif s >= last:
        last = e
        cnt += 1

print(cnt)