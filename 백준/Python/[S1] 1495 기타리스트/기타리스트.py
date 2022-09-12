import sys
input = sys.stdin.readline

# N: 곡 개수, S: 시작 볼륨, M: 최대 볼륨
N, S, M = map(int, input().split())

# 곡 시작 전에 바꿀 수 있는 볼륨 리스트
V = list(map(int, input().split()))

# i번째 곡에서 사용할 수 있는 볼륨 (0번째는 시작 볼륨)
vol = [list() for i in range(N + 1)]

vol[0].append(S)

# i번째 곡 사용할 수 있는 볼륨 구하기
for i in range(1, N + 1):

    # 이전 곡에서 사용할 수 있었던 볼륨에서 V[i - 1]를 더하고 뺀 값
    for j in range(len(vol[i - 1])):
        tmp1 = vol[i - 1][j] + V[i - 1]
        tmp2 = vol[i - 1][j] - V[i - 1]

        # 볼륨이 범위 안에 속하면 리스트에 추가
        if (0 <= tmp1 <= M) and (tmp1 not in vol[i]):
            vol[i].append(tmp1)
        if (0 <= tmp2 <= M) and (tmp2 not in vol[i]):
            vol[i].append(tmp2)

# 값이 없다면 연주 불가
if len(vol[N]) == 0:
    print(-1)
else:
    print(max(vol[N]))
