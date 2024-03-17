from collections import defaultdict
import sys
input = sys.stdin.readline

# 공 개수
N = int(input())

# 모든 공의 색과 크기, 인덱스 (크기 순으로 오름차순 정렬)
balls = sorted([list(map(int, input().split())) + [i] for i in range(N)], key = lambda x: x[1])

# 각 공이 잡을 수 있는 공들의 크기 합
res = [0] * N

# 각 색깔별 공의 크기 누적합
color = defaultdict(int)

# 총합
total = 0

# 비교 공
j = 0

# 기준 공
for i in range(N):
    # 현재 크기보다 작은 공 탐색
    while balls[j][1] < balls[i][1]:
        total += balls[j][1]
        color[balls[j][0]] += balls[j][1]
        j += 1

    # 현재 공이 잡을 수 있는 공들의 크기 합
    res[balls[i][2]] = total - color[balls[i][0]]

# 결과 출력
for i in res:
    print(i)