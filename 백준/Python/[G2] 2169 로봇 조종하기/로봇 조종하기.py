from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# N X M 크기의 지형
N, M = map(int, input().split())

# 각 위치에서의 최대 가치
value = [list(map(int, input().split())) for _ in range(N)]
# 0행은 오른쪽으로만 이동할 수 있으므로 최대 가치 갱신
for i in range(1, M):
    value[0][i] += value[0][i - 1]

# 1행부터 한 행씩 탐색
for i in range(1, N):
    # 왼쪽에서 오른쪽으로 가는 경우와 오른쪽에서 왼쪽으로 가는 경우 나눠서 탐색
    left_to_right, right_to_left = value[i][:], value[i][:]

    # 왼쪽 -> 오른쪽
    for j in range(M):
        # 0열은 위에서 내려오는 경우밖에 없음
        if j == 0:
            left_to_right[j] += value[i - 1][j]
        # 위에서 내려오는 경우와 왼쪽에서 오는 경우 비교
        else:
            left_to_right[j] += max(value[i - 1][j], left_to_right[j - 1])

    # 오른쪽 -> 왼쪽
    for j in range(M - 1, -1, -1):
        # 마지막 열은 위에서 내려오는 경우밖에 없음
        if j == M - 1:
            right_to_left[j] += value[i - 1][j]
        # 위에서 내려오는 경우와 오른쪽에서 오는 경우 비교
        else:
            right_to_left[j] += max(value[i - 1][j], right_to_left[j + 1])

    # 왼쪽에서 오른쪽으로 가는 경우와 오른쪽에서 왼쪽으로 가는 경우를 비교하여 최대 가치 저장
    for j in range(M):
        value[i][j] = max(left_to_right[j], right_to_left[j])

print(value[N - 1][M - 1])