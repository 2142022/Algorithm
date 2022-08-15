#회의 수 입력받기
N = int(input())
arr = []

#각 회의 시간 입력받기
arr = [list(map(int, input().split())) for n in range(N)]

#arr정렬(시작 시간 기준으로 정렬 후 끝나는 시간 기준으로 정렬)
arr.sort(key=lambda arr: arr[0])
arr.sort(key=lambda arr: arr[1])

cnt = 0
start = 0

for i,j in arr:
    if i >= start:
        cnt += 1
        start = j

print(cnt)

