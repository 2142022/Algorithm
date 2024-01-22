import sys
input = sys.stdin.readline

# 주어진 수
N = int(input())

# 경우의 수 (자기 자신 포함하므로 무조건 1가지 경우의 수 존재)
cnt = 1

# 시작 수, 끝 수, 연속한 수들의 합
start, end, s = 1, 2, 3
while start < end < N:
    # 연속한 수들의 합이 N보다 작은 경우 end를 높이기
    if s < N:
        end += 1
        s += end

    # 연속한 수들의 합이 N보다 큰 경우 start를 높이기
    elif s > N:
        s -= start
        start += 1

    # 연속한 수들의 합이 N인 경우 경우의 수 +1
    else:
        cnt += 1
        end += 1
        s += end - start
        start += 1

print(cnt)