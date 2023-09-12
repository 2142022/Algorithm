import sys
input = sys.stdin.readline

# N: 동굴의 길이, H: 동굴의 높이
N, H = map(int, input().split())

# cnt1[i]: 구간 i에 있는 석순의 개수
cnt1 = [0] * (H + 1)
# cnt2[i]: 구간 H - 1 - i에 있는 종유석의 개수
cnt2 = [0] * (H + 1)

# 각 장애물의 길이 탐색
for i in range(N):
    # 장애물의 길이
    l = int(input())

    # 석순
    if i % 2 == 0:
        cnt1[l] += 1

    # 종유석
    else:
        cnt2[l] += 1

# 정확한 장애물의 개수 세기
for i in range(H - 1, -1, -1):
    cnt1[i] += cnt1[i + 1]
    cnt2[i] += cnt2[i + 1]

# 개똥벌레가 파괴해야 하는 장애물의 최소 개수
obstacle = sys.maxsize
# 최소 개수의 장애물이 있는 구간의 개수
part = 0

# 모든 구간 탐색
for i in range(1, H + 1):
    # 현재 구간의 장애물 개수
    cnt = cnt1[i] + cnt2[H + 1 - i]

    # 기존 최소 개수와 같은 경우
    if cnt == obstacle:
        part += 1
    # 기존 최소 개수보다 적은 경우
    elif cnt < obstacle:
        obstacle = cnt
        part = 1

print(obstacle, part)