import sys
input = sys.stdin.readline

# 일의 개수 입력받기
N = int(input())

# 각 일마다 필요한 시간, 끝내야 하는 시간
work = [list(map(int, input().split())) for i in range(N)]

# S 기준으로 내림차순 정렬
work.sort(key = lambda a : a[1], reverse = True)

for i in range(len(work) - 1):
    # 시간 내에 끝낼 수 없으면 다음 일의 필요한 시간에 추가
    if work[i][0] > work[i][1] - work[i+1][1]:
        work[i+1][0] += work[i][0] - (work[i][1] - work[i+1][1])

# 처음 일을 시간내에 끝낼 수 있다면 가장 늦게 일어나도 되는 시간
if work[N - 1][0] <= work[N - 1][1]:
    print(work[N - 1][1] - work[N - 1][0])
else:
    print(-1)
