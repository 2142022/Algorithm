import sys
input = sys.stdin.readline

# 땅 크기, 인벤토리에 있는 블록 개수
N, M, B = map(int, input().split())

# 땅 높이별 개수
cnt = [0] * 257
# 최저 높이, 최대 높이
min_h, max_h = 256, 0
for _ in range(N):
    row = list(map(int, input().split()))
    for h in row:
        cnt[h] += 1
        min_h = min(min_h, h)
        max_h = max(max_h, h)

# 땅 높이가 모두 같아지는 최소 시간
min_time = sys.maxsize

# 가능한 높이 중 최대 높이
result_h = 0

# 맞출 땅의 높이
for h in range(min_h, max_h + 1):
    # 땅 높이를 h로 만드는데 걸리는 시간
    time = 0

    # 인벤토리에 있는 블록 개수
    block = B
    for i in range(max_h, min_h - 1, -1):
        c = cnt[i]

        # 같은 높이는 패스
        if i == h:
            continue

        # 필요한 만큼 쌓기
        elif i < h:
            b = (h - i) * c
            # 인벤토리에 있는 블록이 부족한 경우 끝내기
            if block < b:
                break
            time += b
            block -= b

        # 더 높은 만큼 인벤토리에 넣기
        else:
            b = (i - h) * c
            time += 2 * b
            block += b

    # 최소 시간, 최대 높이 비교
    else:
        if time < min_time:
            min_time = time
            result_h = h
        elif time == min_time:
            result_h = h

print(min_time, result_h)