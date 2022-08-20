import sys
input = sys.stdin.readline

# 마을 개수
N = int(input())

# 마을 위치 및 각 마을의 사람 수
town = [list(map(int, input().split())) for i in range(N)]

# 마을 위치 순으로 오름차순 정렬
town.sort()

# 마을 사람 수의 합
p_sum = 0
for i in range(N):
    p_sum += town[i][1]

# 마을 사람 수의 중간값
i = 0
tmp = 0
while True:
    tmp += town[i][1]
    if tmp >= p_sum / 2:
        break
    i += 1

# 마을 사람 수의 중간값이 있는 마을의 위치 출력
print(town[i][0])
