import sys
input = sys.stdin.readline

# 벽돌의 수
N = int(input())

# 벽돌의 번호가 1번부터 시작하므로 앞에 빈 배열을 넣어주기
block = [[0,0,0,0]]
for i in range(1, N+1):
    area, height, weight = map(int, input().split())
    block.append([i, area, height, weight])

# 벽돌을 밑면 넓이 순으로 오름차순 정렬
block.sort(key = lambda x: x[1])

# top[i] = i번 벽돌을 가장 아래에 두었을 때 만들 수 있는 탑의 최대 높이
top = [0] * (N+1)

# 탑의 꼭대기에서부터 아래로 하나씩 만들기
for i in range(1, N+1):
    # i번째 벽돌의 면적보다 작은 벽돌만 확인하면 됨
    for j in range(0, i):
        # i번째 벽돌보다 무게가 더 작다면 아래로 탑을 쌓을 수 있으므로 max 비교
        if block[j][3] < block[i][3]:
            top[i] = max(top[i], top[j] + block[i][2])

# 탑의 최대 높이
max_height = max(top)

# 탑의 최대 높이가 있는 인덱스
idx = top.index(max_height)

# 최대 높이의 탑을 만들 때 필요한 벽돌들의 번호
result = []

# 탑의 높이를 이용하여 벽돌의 번호 구하기
while idx != 0:
    if max_height == top[idx]:
        result.append(block[idx][0])
        max_height -= block[idx][2]
    idx -= 1

# 탑을 쌓을 때 필요한 벽돌의 개수
print(len(result))

# 탑의 꼭대기부터 벽돌의 번호 하나씩 출력
for i in range(len(result) - 1, -1, -1):
    print(result[i])
