import sys
input = sys.stdin.readline

# 색종이가 있는 부분은 1, 없는 부분은 0
paper = 0

# 색종이 수
N = int(input())
for _ in range(N):
    # 도화지의 왼쪽에서부터의 거리, 도화지의 아래쪽에서부터의 거리
    l, d = map(int, input().split())

    # 색종이 체크
    for i in range(l, l + 10):
        for j in range(d, d + 10):
            paper |= 1 << (100 * i + j)

# 사방 탐색용
di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)

# 검은 영역의 둘레의 길이
result = 0
for i in range(100):
    for j in range(100):
        # 현재 위치에 색종이가 있고 사방의 색종이 개수가 2개 이상 3개 이하인 경우 둘레
        if paper & 1 << (100 * i + j):
            cnt = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= 100 * ni + nj < 10000 and paper & 1 << (100 * ni + nj):
                    cnt += 1

            # 사방에 색종이가 3개 있는 경우, 모서리이므로 1번 카운트
            if cnt == 3:
                result += 1

            # 사방에 색종이가 2개 있는 경우, 꼭짓점이므로 2번 카운트
            elif cnt == 2:
                result += 2

print(result)